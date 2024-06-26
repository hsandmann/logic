
Os números são elementos fundamentais para a matemática, pois, são utilizados para representar quantidades, medidas, grandezas, entre outros. Os números são classificados em diferentes conjuntos, conforme a sua natureza e propriedades. Os principais conjuntos numéricos são: [naturais](#naturais), [inteiros](#inteiros), [racionais](#racionais), [irracionais](#irracionais), [reais](#reais) e [complexos](#complexos).


## [Naturais](#naturais)

Os números naturais é o conjunto de números que permite contagem de elementos da Natureza. Partindo do número $1$, todos os elementos encontrados na Natureza podem ser enumerados, assim, conforme destacado por Euclides em sua obra "Os Elementos"[^1], os números naturais são infinitos, pois, a partir do número $1$. A partir do número $1$, os demais elementos são obtidos por sucessão. Os números naturais são representados por $\mathbb{N}$ e são infinitos.

$$
\mathbb{N} = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, \ldots\}
$$

Alguns autores, ao definir os números naturais, incluem o zero, $0$, como: 

$$
\mathbb{N} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, \ldots\}
$$

Mas esse é um tema controverso, pois, o zero, $0$, é um número que representa a ausência de elementos, ou seja, não é um número que permite a contagem de elementos. O zero não existia na matemática antiga, e foi introduzido na matemática ocidental por volta do século VII, por meio dos matemáticos indianos, que o utilizavam para representar a ausência de elementos[^2].


## [Inteiros](#inteiros)

Os números inteiros são o conjunto de números que incluem os números naturais, seus opostos e o zero. Os números inteiros são representados por $\mathbb{Z}$ e são infinitos. Os números inteiros contém os números opostos, ou seja, para cada número natural, existe um número inteiro negativo correspondente, cuja a soma com o natural resulta em zero. Exemplo de conjunto de números inteiros:

$$
\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}
$$

Note que não **existem números negativos na Natureza**, mas, os números negativos são utilizados para representar grandezas opostas, como, por exemplo, a temperatura, onde o zero grau Celsius representa a temperatura de congelamento da água, e os números negativos representam temperaturas abaixo de zero. Logo, para representar números negativos, foi necessário anotar o sinal de menos, $-$, antes do número natural correspondente.

!!! tip "Representação"

    Se não existêm números negativos na Natureza, então, como representá-los no formato binário? Ou seja, através de $0$s e $1$s. A representação de números negativos é realizada por meio do complemento de dois, que é uma técnica utilizada para representar números negativos em binário.

## [Racionais](#racionais)

Os números racionais são o conjunto de números que podem ser representados por frações, ou seja, são números que podem ser expressos na forma de:

$$
\frac{p}{q}
$$

onde $p$ e $q$ são números inteiros e $q \neq 0$. Os números racionais são representados por $\mathbb{Q}$ e são infinitos. Exemplo de conjunto de números racionais:

$$
\mathbb{Q} = \left\{\ldots, \frac{3}{-4}, \frac{-2}{3}, \frac{-1}{2}, \frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \ldots\right\}
$$

Logo, caso se queira replicar tal número em qualquer outro local, basta anotar os inteiros $p$ e $q$ e realizar a operação de divisão novamente, assim, o mesmo número será obtido.

A mesma regra vale para toda **dízima periódica**, que é uma fração que possui um número finito de algarismos decimais, seguido de uma sequência infinita de algarismos decimais repetidos. Exemplo de dízima periódica:

$$
\begin{align}
    \frac{10}{3} & = 3,333333333333333… \\
    \frac{1}{7} & = 0,14285714285714285…
\end{align}
$$

??? warning "Dízima Periódica"

    Todas as **dízimas periódicas**, possuem padrão de repetição, são **números racionais**.


## [Irracionais](#irracionais)

Os números irracionais é o conjunto que mostra que a Natureza não pode ser domanda pela matemática, ou seja, são números que não podem ser representados por frações. Os números irracionais são representados por $\mathbb{I}$ e são infinitos. Exemplo de conjunto de números irracionais:

$$
\mathbb{I} = \left\{\sqrt{2}, \pi, e, \ldots\right\}
$$

Não é possível anotar um número irracional em um papel e carregá-lo para outro local, pois, os números irracionais são infinitos e não periódicos, ou seja, não possuem um padrão de repetição.

!!! info "Caso $\pi$"

    O número $\pi$ é um exemplo de número irracional, pois, é um número que representa a razão entre o perímetro de uma circunferência e o seu diâmetro, e possui infinitas casas decimais, sem um padrão de repetição.


!!! info "Caso $\sqrt{2}$"

    $H$: assumindo que todo número pode ser racionalizado, então, podemos assumir que para o seguinte número existe um racional que o calcula:

    $$ \sqrt{2} = \frac{p}{q} $$

    onde $p, q \in \mathbb{Z}$. Logo,

    $$
    \begin{align}
        \sqrt{2} &= \frac{p}{q} \\
        \left( \sqrt{2} \right)^{2} &= \left( \frac{p}{q} \right)^{2} \\
        2 &= \left( \frac{p}{q} \right)^{2} \\
        2 &= \frac{p^{2}}{q^{2}} \\
        2q^{2} &= p^{2} \\
    \end{align}
    $$

    Ora, obrigatoriamente, $p$ e $q$ são inteiros, note que a expressão $2q^{2} = p^{2}$ é impossível, já que um dos lados da iqualdade é necessariamente **par** sem que o outro lado o seja. Portanto, não existe tal razão de inteiros $\displaystyle \frac{p}{q}$ que calcule $\sqrt{2}$.

    Conseqüentemente, $\sqrt{2}$ é irracional, $\mathbb{I}$.

!!! info "Caso $\log_{2}{3}$"

    $H$: assumindo que todo número pode ser racionalizado, então, podemos assumir que para o seguinte número existe um racional que o calcula:

    $$ \log_{2}{3} = \frac{p}{q} $$

    onde $p, q \in \mathbb{Z}$. Logo,

    $$
    \begin{align}
        2^{\frac{p}{q}} &= 3 \\
        \left(2^{\frac{p}{q}}\right)^q &= 3^q \\
        2^{p} &= 3^q
    \end{align}
    $$

    Ora, obrigatoriamente, $p$ e $q$ são inteiros, note que a expressão $2^{p} = 3^q$ é impossível, já que um dos lados da iqualdade é necessariamente **par** e o outro é necessariamente **ímpar**. Se fatorar o lado esquerdo, haverá um termo múltiplo de $2$, o mesmo não acontece com o lado direito. Portanto, não existe tal razão de inteiros $\displaystyle \frac{p}{q}$ que calcule $\log_{2}{3}$.

    Conseqüentemente, $\log_{2}{3}$ é irracional, $\mathbb{I}$.

Números que aparecem em diversos cenários - que são irracionais - portanto, podem ser definidos de maneira "racional":

| símbolo | | aproximação | valor |
|:---:||:---|:-|
| $Π$ || $\displaystyle \frac{C}{d}$ | 3,141592653589793... |
| $e$ || $\displaystyle \sum_{n=0}^{\infty}\frac{1}{n!} \approx \left( \frac{n+1}{n} \right) ^ n$ | 2,718281828459045... |
| $𝜑$ || $\displaystyle \frac{1+\sqrt{5}}{2}$ | 1,618033988749895... |
| || $\sqrt{2}$ | 1,414213562373095... |
| || $\displaystyle \log_2{3}$ |1,584962500721156... |

??? warning "Dízima Não Periódica"

    **Dízimas não periódicas**, ou seja, sem padrão de repetição, também **são irracionais**.

!!! tip "Representação"

    Existêm números irracionais na Natureza, então, como representá-los no formato binário? Ou seja, através de $0$s e $1$s. A representação de números irracionais é um problema em binário, por isso, existe uma padronização criada para representar os números $\mathbb{R}$ como um todo.


## [Reais](#reais)

Como nem todo número pode ser escrito pela razão de dois números inteiros, motivo pelo qual existêm os irracionais - $\mathbb{P}$, a disjunção desses dois conjuntos. Logo,

$$\mathbb{R} = \mathbb{Q} \lor \mathbb{P}$$


## [Complexos](#complexos)

$\mathbb{C}$


[^1]: Bicudo, Irineu., Euclides. [Os elementos](https://www.amazon.com.br/Os-elementos-Irineu-Bicudo/dp/8571399352){target='_blank'}. Brasil: Editora Unesp, 2009.
[^2]: Aczel MR, Aczel D and Ville M (2019) [Hero From the East: How Zero Came to the West](https://doi.org/10.3389/frym.2019.00128){target='_blank'}. Front. Young Minds. 7:128. [doi: 10.3389/frym.2019.00128](https://doi.org/10.3389/frym.2019.00128){target='_blank'}.