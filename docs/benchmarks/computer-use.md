# Computer Use Benchmark (CUB) Performance

## Overview of CUB Benchmark

The Computer Use Benchmark (CUB) is a challenging evaluation framework designed to assess AI agents' capabilities in real-world computer usage scenarios. This benchmark is particularly significant as it tests agents' abilities in economically valuable domains like accounting, healthcare, finance, and other professional tasks.

## Performance Comparison

Here's how different models perform across various domains:

| Model | Business Operations | Construction | Consumer | Finance | Healthcare | Supply Chain | Overall |
|-------|-------------------|--------------|----------|----------|------------|--------------|----------|
| Manus | 10.59% | 16.00% | 17.00% | 7.06% | 0.00% | 4.10% | 9.23% |
| OpenAI CUA | 14.60% | 19.00% | 7.41% | 2.73% | 4.86% | 5.14% | 7.28% |
| Claude (Computer Use) | 6.33% | 19.50% | 12.06% | 2.03% | 0.00% | 0.85% | 6.01% |
| Claude (Browser Use) | 6.92% | 11.00% | 6.40% | 0.00% | 0.36% | 3.50% | 3.78% |
| Gemini 2.5 Pro | 1.41% | 0.00% | 1.50% | 0.20% | 0.00% | 0.00% | 0.56% |

## Key Evaluation Areas

The benchmark evaluates critical capabilities required for real-world tasks:

1. **Long-sequence Memory**
   - Following complex multi-step instructions
   - Maintaining context across extended operations

2. **Multi-application Coordination**
   - Seamless switching between different software
   - Data transfer between applications
   - Interface adaptation

3. **Task Reliability**
   - Consistent performance in repetitive tasks
   - Error handling and recovery
   - Maintaining accuracy over time

4. **Interface Navigation**
   - Handling unfamiliar interfaces
   - Working with domain-specific tools
   - Adapting to different UI paradigms

## Example Tasks

### Construction Domain Example
Task: Property Square Footage Calculation
- Navigate and utilize block maps
- Multimodal reasoning for diagram interpretation
- Long-sequence memory application
- Complex spatial calculations

### Healthcare Domain Example
Task: EHR Data Entry
- Parse medical documentation
- Navigate complex EHR interfaces
- Handle hidden functionality
- Medical terminology comprehension
- Data entry in multi-panel interfaces

## Technical Infrastructure

The benchmark leverages advanced evaluation infrastructure:
- Parallelized testing environments
- VM snapshotting for efficient evaluation
- Support for both browser and desktop configurations
- Rich action space compatibility
- Black-box agent system support

## TODO

- [ ] Add GenZ performance metrics across all domains
- [ ] Implement automated testing pipeline for CUB
- [ ] Develop domain-specific optimization strategies
- [ ] Create detailed performance analysis dashboards
- [ ] Document best practices for each domain
