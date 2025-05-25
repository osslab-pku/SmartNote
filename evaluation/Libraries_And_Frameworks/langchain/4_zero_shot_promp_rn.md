# Release Notes for langchain-openai 0.1.22

## New Features and Improvements

1. **Embeddings Enhancements**:
   - Added dimension support to `ZhipuAIEmbeddings` for models `embedding-3` and later, allowing users to specify the dimensions parameter. This enhancement is accompanied by a new test case for the `embedding-3` model.

2. **Documentation Updates**:
   - Standardized and improved documentation for various components, including OpenAI, ChatBaichuan, QianfanChatEndpoint, ChatSparkLLM, and ChatZhipuAI.
   - Updated API reference links and installation instructions for several integrations, including Qdrant, Gmail Toolkit, and others.
   - Added new documentation for Upstash Vector integration, detailing the use of namespaces and metadata filtering.
   - Improved the document loaders index and tools index table for better navigation and understanding.

3. **Deprecations and Replacements**:
   - Deprecated `langchainhub` in favor of `langsmith sdk` for pulling prompts, with a fallback to `langchainhub`.
   - Replaced `SqliteSaver` with `MemorySaver` in the Conversational RAG tutorial to match LangGraph v2 documentation.

4. **Bug Fixes**:
   - Fixed a pip install bug in the cookbook related to the `unstructured[all-docs]` package.
   - Corrected various typos and grammatical errors across multiple documentation files.
   - Resolved a divide by zero error in the semantic chunker within the experimental module.

5. **API and Integration Updates**:
   - Updated API reference documentation for several embeddings models, including OpenAI, MistralAI, TogetherAI, Fireworks, and AI21.
   - Implemented standard tracing parameters for LLMs and retrievers to enhance debugging and performance tracking.

6. **Community Contributions**:
   - Added `args_schema` to the `SearxSearchResults` tool to fix JSON serialization issues.
   - Improved asynchronous methods for AzureSearch VectorStore, addressing issues with asynchronous iterators.

7. **Miscellaneous**:
   - Updated integration docs for various providers, including Cohere, Fireworks, and OpenAI.
   - Enhanced the document loader for custom implementations, ensuring better compatibility and performance.

This release focuses on enhancing the flexibility and usability of embeddings, improving documentation, and addressing several bugs and issues reported by the community. The updates aim to provide a more robust and user-friendly experience for developers working with the langchain-openai library.