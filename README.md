# biolink-model-pydantic
Pydantic dataclasses for the Biolink model


#### Installation

```
pip install biolink_model_pydantic
```

#### Using the dataclasses

```python
from biolink_model_pydantic.model import Gene

gen_entity = Gene(id='NCBIGene:123', in_taxon='NCBITaxon:9606')
```
