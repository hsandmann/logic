

Operações com conjuntos são fundamentais para a resolução de problemas em diversas áreas do conhecimento. A teoria dos conjuntos é um ramo da matemática que estuda conjuntos, que são coleções de objetos. A teoria dos conjuntos é uma parte da matemática que lida com a definição, propriedades e operações de conjuntos.

=== "Source"

    ```python
    --8<-- "docs/snippets/script.py"
    ```

=== "Result"

    ```python exec="on" html="1"
    --8<-- "docs/snippets/script.py"
    ```


```pyodide install="cowsay,matplotlib"
--8<-- "docs/snippets/pyod.py"
```


!!! info "Markov"

    As cadeias de Markov são um modelo matemático que descreve um sistema que transita entre estados discretos. Elas são amplamente utilizadas em diversas áreas, como estatística, ciência da computação e teoria da informação.

    === "Source"

        ```python
        --8<-- "docs/snippets/markov.py"
        ```

    === "Result"

        ```python exec="on" html="1"
        --8<-- "docs/snippets/markov.py"
        ```


Exercícios
---

=== notes "Entrega"

    Projeto integrador:

    - Levantar os dados de um problema real que envolva conjuntos e operações com conjuntos.
    - Classificar os dados em conjuntos, dimensões.
    - Tratar os dados.
    - Normalizar os dados.
    - Buscar uma dimensão que ofereça maior separabilidade entre as dimensões.
    



``` plotly
{
    "data": [
        {
            "x": ["giraffes", "orangutans", "monkeys"],
            "y": [20, 14, 23],
            "type": "line"
        }
    ]
}
```

``` plotly
{
    "data": [
    {
        type: "sankey",
        orientation: "h",
        node: {
            pad: 15,
            thickness: 30,
            line: {
                color: "black",
                width: 0.5
            },
            label: ["A1", "A2", "B1", "B2", "C1", "C2"],
            color: ["blue", "blue", "blue", "blue", "blue", "blue"]
        },
        link: {
            source: [0,1,0,2,3,3],
            target: [2,3,3,4,4,5],
            value:  [8,4,2,8,4,2]
        }
    }],
    "layout": {
        title: {
            text: "Basic Sankey"
        },
        font: {
            size: 10
        }
    }
}
```



