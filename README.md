# Projeto de Reconhecimento de Entidades Nomeadas
O objetivo deste projeto é desenvolver uma aplicação que identifica e extrai automaticamente entidades específicas contidas num texto, como pessoas, locais e organizações. Para isso foi feito *fine-tuning* do modelo BERTimbau para a tarefa de *Named Entity Recognition* (NER) usando um *dataset* criado com informações consolidadas de diversos arquivos em português.

Colab para visualização das etapas: https://colab.research.google.com/drive/1t5wUG_S76VWsfAgOXoKYWpfSrJdKEXQv?usp=sharing .

## Dataset
O dataset usado para o treinamento pode ser acessado aqui: https://huggingface.co/datasets/lfcc/portuguese_ner .

**Variáveis**:
- `tokens`: Amostras de textos.
- `ner_tags`: Representação de *tags* de cada *token* do texto.

**Tags**:

0. **O** representa *tokens* que não são entidades
1. **B-Data** representa o *token* inicial para datas
2. **I-Data** representa o *token* intermediário para datas
3. **B-Local** representa o *token* inicial para locais
4. **I-Local** representa o *token* intermediário para locais
5. **B-Organizacao** representa o *token* inicial para organizações
6. **I-Organizacao** representa o *token* intermediário para organizações
7. **B-Pessoa** representa o *token* inicial para pessoas
8. **I-Pessoa** representa o *token* intermediário para pessoas
9. **B-Profissao** representa o *token* inicial para profissões
10. **I-Profissao** representa o *token* intermediário para profissões

## Bibliotecas
- `datasets`: Carregamento e manipulação de datasets.
- `transformers`: Uso e fine-tuning de modelos pré-treinados.
- `accelerate`: Treinamento eficiente de modelos.
- `seqeval`: Avaliação de modelos.
- `streamlit`: Criação de aplicação web interativa.

## Modelo
O modelo-base usado pode ser acessado aqui: https://huggingface.co/neuralmind/bert-base-portuguese-cased .

Hiperparâmetros de *fine-tuning*:
* `learning_rate = 0.00002`
* `batch_size = 16`
* `num_train_epochs = 4`
* `weight_decay = 0.01`

## Resultados
| Classe        | Precision | Recall | F1-score | Suport |
|---------------|-----------|--------|----------|---------|
| Data          | 0.99      | 0.99   | 0.99     | 2109    |
| Local         | 0.98      | 0.98   | 0.98     | 2593    |
| Organizacao   | 0.72      | 0.85   | 0.78     | 203     |
| Pessoa        | 0.97      | 0.98   | 0.97     | 2028    |
| Profissao     | 0.79      | 0.85   | 0.82     | 231     |
| **Micro avg** | 0.96      | 0.98   | 0.97     | 7164    |
| **Macro avg** | 0.89      | 0.93   | 0.91     | 7164    |
| **Weighted avg** | 0.96   | 0.98   | 0.97     | 7164    |

* F1-score: 0.9701337398655671
* Acurácia: 0.9832975279130988

## Aplicação
![image](https://github.com/user-attachments/assets/7ae8ec78-2e55-493e-ad08-f938b66b5447)

* Vídeo de apresentação: 
