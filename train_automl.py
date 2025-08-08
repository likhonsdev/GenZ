import os
import json
import yaml
from google.cloud import aiplatform
from google.cloud.aiplatform import AutoMLTextTraining

def load_config(config_path='config/automl_config.yaml'):
    """Load configuration from YAML file."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def init_vertex_ai():
    """Initialize Vertex AI client."""
    aiplatform.init(
        project=os.getenv("GCP_PROJECT_ID"),
        location=os.getenv("GCP_REGION")
    )

def train_model(config):
    """Train model using AutoML on Vertex AI."""
    dataset_config = config['datasetConfig']
    training_config = config['trainingConfig']
    
    dataset = aiplatform.TextDataset.create(
        display_name=dataset_config['datasetDisplayName'],
        gcs_source=dataset_config['gcsSource']['uri']
    )

    job = AutoMLTextTraining(
        display_name="genz_training_job",
        prediction_type="classification",
        multi_label=False,
        dataset=dataset,
        model_display_name=config['modelType'],
        training_fraction_split=config['evaluationConfig']['splitRatio']['training'],
        validation_fraction_split=config['evaluationConfig']['splitRatio']['validation'],
        test_fraction_split=config['evaluationConfig']['splitRatio']['test'],
    )

    model = job.run(
        parent_model=None,
        budget_milli_node_hours=training_config['budgetMilliNodeHours'],
        disable_early_stopping=False
    )

    return model

def deploy_model(model, config):
    """Deploy trained model to endpoint."""
    endpoint_config = config['vertexEndpoint']
    endpoint = model.deploy(
        machine_type=endpoint_config['machineType'],
        min_replica_count=endpoint_config['minReplicaCount'],
        max_replica_count=endpoint_config['maxReplicaCount']
    )
    
    return endpoint

if __name__ == "__main__":
    config = load_config()
    init_vertex_ai()
    model = train_model(config)
    endpoint = deploy_model(model, config)
    
    # Log model metrics
    metrics = model.get_metrics()
    print(f"Model evaluation metrics: {metrics}")
    
    # Save model info
    model_info = {
        "model_id": model.name,
        "endpoint_id": endpoint.name,
        "metrics": metrics
    }
    
    with open("GenZ-checkpoints/model_info.json", "w") as f:
        json.dump(model_info, f, indent=2)
