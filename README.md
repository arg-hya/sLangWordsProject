# Large scale non-standard English database and Transformer based translation system

## Abstract
Natural Language Processing (NLP) faces challenges
in understanding and processing region- or industry-specific
language. In real-world scenarios, conversational language used
in blogs and social media platforms often contains slang and
non-standard words (SNSW). These unconventional terms are
not typically present in curated datasets used to train NLP
models. As a consequence, the performance of these models is
significantly affected when dealing with such real-world linguistic
variations. This paper proposes a novel solution to address this
limitation, allowing existing NLP models to better handle the
incorporation of SNSW and improve their understanding and
processing capabilities in diverse linguistic contexts.
The study introduces UrbanDB, an automatically curated,
large-scale lexical database regularly updated from crowdsourced
dictionaries. UrbanDB provides comprehensive and continuously
updated information on SNSW, including example
sentences and their formal English synonyms. Additionally, a
transformer-based translation system is developed to convert
English articles containing SNSW into standard English articles.
These translated articles can be used by downstream NLP models
or human reviewers to enhance understanding and readability.
Three experiments are conducted to validate the proposed approach.
The first experiment demonstrates the high accuracy
of the model for detecting SNSW, while the second experiment
evaluates the translation of text containing SNSW. Finally, the
third showcases the performance enhancement of a pre-trained
NLP model when the proposed solution was incorporated into
the pipeline. Additionally, the paper emphasizes the system’s easy
integration into NLP pipelines and its potential for extension to
other domains and languages.

## Sample translation
<kbd>
  <img src="/image/image.png">
</kbd>

