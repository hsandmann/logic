

## Curso de Cálculo: De Limites a Derivadas, Passando por Logaritmos

### Módulo 1: Limites

#### 1.1 Introdução aos Limites
- **O que é um limite?**: Um limite descreve o comportamento de uma função à medida que a variável independente se aproxima de um determinado valor. Ele é a base para entender continuidade e derivadas.
- **Notação**: \(\lim_{x \to a} f(x) = L\) significa que, conforme \(x\) se aproxima de \(a\), \(f(x)\) se aproxima de \(L\).
- **Exemplo**: \(\lim_{x \to 2} (x + 3) = 5\), pois substituir \(x = 2\) diretamente funciona.


```python exec="on" html="1"
--8<-- "docs/limits/python/limit.def.py"
```


#### Propriedades dos Limites

1. Unicidade dos Limites: o limite, se existir, **é único**.

1. $\displaystyle \lim_{x \to a} = P(x) = P(a)$, onde $P(x) = \text{polinômio}$

    eg.:

    i) $\displaystyle \lim_{x \to 2}(3x-1) = 5$

    ii) $\displaystyle \lim_{x \to 1}(x^5 -3x^2 + 2) = 0$

1. Se $\displaystyle \lim_{x \to a}f(x)$ e $\displaystyle \lim_{x \to a}g(x)$ existem **E** $\in \mathbb{R}$

    a) $\displaystyle \lim_{x \to a} [f(x) \pm g(x)] = \lim_{x \to a} f(x) \pm \lim_{x \to a} g(x)$

    b) $\displaystyle \lim_{x \to a} [c . f(x)] = c. \left( \lim_{x \to a} f(x) \right)$

    c) $\displaystyle \lim_{x \to a} [f(x) . g(x)] = \lim_{x \to a} f(x) . \lim_{x \to a} g(x)$

    d) $\displaystyle \lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)} {\lim_{x \to a} g(x)}, \lim_{x \to a} g(x) \neq 0$

    e) $\displaystyle \lim_{x \to a} [f(x)]^n = \left[ \lim_{x \to a} f(x)\right]^n$

    f) $\displaystyle \lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{\lim_{x \to a} f(x) }$

    g) $\displaystyle \lim_{x \to a} [\ln f(x)] = \ln \left( \lim_{x \to a} f(x) \right)$

    h) $\displaystyle \lim_{x \to a} [\sin f(x)] = \sin \left( \lim_{x \to a} f(x) \right)$

    i) $\displaystyle \lim_{x \to a} [\cos f(x)] = \cos \left( \lim_{x \to a} f(x) \right)$

    j) $\displaystyle \lim_{x \to a} \left[e^{f(x)}\right] = e^{\lim_{x \to a} f(x)}$


1. Propriedade:
    
    $f(x) \le g(x) \le h(x)$
    
    para todo $x$ em algum intervalo aberto contendo $a$ e
    
    $\displaystyle \lim_{x \to a} f(x) = L = \lim_{x \to a} h(x)$,

    então,

    $\displaystyle \lim_{x \to a} g(x) = L$.

    eg.:

    $$
    \begin{align*}
      \lim_{x \to 0} x^2.\left|\sin \frac{1}{x}\right| \\
      & \sin\frac{1}{x} \in [-1; 1] \therefore \left| \sin\frac{1}{x}\right| \in [0; 1] \\
      = \lim_{x \to 0} x^2 . \left( 0 \le \left| \sin\frac{1}{x} \right| \le 1 \right) \\
      = \lim_{x \to 0} \left[ 0 \le \left| x^2 . \sin\frac{1}{x}\right| \le x^2 \right] \\
      \lim_{x \to 0} 0 \le \lim_{x\to0} \left| x^2 . \sin\frac{1}{x}\right| \le \lim_{x\to0} x^2 \\
      0 \le \lim_{x\to0} \left| x^2 . \sin\frac{1}{x}\right| \le 0 \\
      f(x) \le g(x) \le h(x) \\
      \cancelto{0}{f(x)} \le g(x) \le \cancelto{0}{h(x)} \\
      & \therefore g(x) \to 0 \\
      & \therefore g(x) = \lim_{x\to0} \left| \sin\frac{1}{x}\right| = 0 \\
    \end{align*}
    $$

    Em modo simplificado:

    \begin{align}
    & \lim_{x \to 0} x^2.\left|\sin \frac{1}{x}\right| \\
    = & \lim_{x \to 0} x^2.\lim_{x \to 0}\left|\sin \frac{1}{x}\right| \\
    = & 0.\cancelto{[0;1]}{\lim_{x \to 0}\left|\sin \frac{1}{x}\right|} \\
    = & 0.\forall[0;1] \\
    = & 0 \\
    \end{align}




#### 1.2 Cálculo de Limites
- **Limites diretos**: Substituímos o valor diretamente quando possível.
- **Técnicas para limites mais complexos**:
  - Fatoração: \(\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = \lim_{x \to 2} \frac{(x - 2)(x + 2)}{x - 2} = \lim_{x \to 2} (x + 2) = 4\).
  - Racionalização: Para expressões com raízes.
- **Limites laterais**: \(\lim_{x \to a^-}\) (pela esquerda) e \(\lim_{x \to a^+}\) (pela direita).

#### 1.3 Limites no Infinito
- **Comportamento assintótico**: Analisamos o que acontece quando \(x \to \infty\) ou \(x \to -\infty\).
- **Exemplo**: \(\lim_{x \to \infty} \frac{2x + 1}{x} = 2\), pois o termo de maior grau domina.

#### 1.4 Formas Indeterminadas
- **Tipos**: \(\frac{0}{0}\), \(\frac{\infty}{\infty}\), etc.
- **Regra de L'Hôpital**: Para \(\frac{0}{0}\), derive o numerador e o denominador. Exemplo: \(\lim_{x \to 0} \frac{\sin x}{x} = \lim_{x \to 0} \frac{\cos x}{1} = 1\).





## Assíntotas

### Verticais
- **Definição**: Uma reta vertical \(x = a\) é uma assíntota vertical se \(\lim_{x \to a} f(x) = \pm \infty\).
- **Exemplo**: \(f(x) = \frac{1}{x - 2}\) tem uma assíntota vertical em \(x = 2\).
- **Cálculo**: Encontre os valores de \(x\) que tornam o denominador zero.
- **Exemplo**: Para \(f(x) = \frac{1}{x^2 - 4}\), as assíntotas verticais são \(x = 2\) e \(x = -2\).
- **Gráfico**: A função se aproxima de \(\infty\) ou \(-\infty\) conforme \(x\) se aproxima de \(a\).
- **Exemplo**: \(f(x) = \frac{1}{x - 1}\) tem uma assíntota vertical em \(x = 1\).
- **Gráfico**: A função se aproxima de \(\infty\) ou \(-\infty\) conforme \(x\) se aproxima de \(a\).
- **Exemplo**: \(f(x) = \frac{1}{x^2 - 4}\) tem assíntotas verticais em \(x = 2\) e \(x = -2\).
- **Gráfico**: A função se aproxima de \(\infty\) ou \(-\infty\) conforme \(x\) se aproxima de \(a\).
- **Exemplo**: \(f(x) = \frac{1}{x^2 - 4}\) tem assíntotas verticais em \(x = 2\) e \(x = -2\).
- **Gráfico**: A função se aproxima de \(\infty\) ou \(-\infty\) conforme \(x\) se aproxima de \(a\).
- **Exemplo**: \(f(x) = \frac{1}{x^2 - 4}\) tem assíntotas verticais em \(x = 2\) e \(x = -2\).


### Inclinadas ou Oblíquas

- **Definição**: Uma reta \(y = mx + b\) é uma assíntota oblíqua se \(\lim_{x \to \infty} [f(x) - (mx + b)] = 0\).

$$
f(x) = y = \frac{2x^3}{x^2 + 4}
$$

```python exec="on" html="1"
--8<-- "docs/limits/python/limit.asymptote.inclined.py"
```



---

### Módulo 2: Continuidade

#### 2.1 Definição de Continuidade
- Uma função \(f(x)\) é contínua em \(x = a\) se:
  1. \(f(a)\) está definida.
  2. \(\lim_{x \to a} f(x)\) existe.
  3. \(\lim_{x \to a} f(x) = f(a)\).
- **Exemplo**: \(f(x) = x^2\) é contínua em todos os reais.

#### 2.2 Tipos de Descontinuidades
- **Removível**: O limite existe, mas \(f(a)\) não é igual ao limite ou não está definido.
- **De salto**: Limites laterais diferentes.
- **Infinita**: A função tende a \(\infty\) ou \(-\infty\).

#### 2.3 Teorema do Valor Intermediário
- Se \(f\) é contínua em \([a, b]\), ela assume todos os valores entre \(f(a)\) e \(f(b)\).

---

### Módulo 3: Logaritmos

#### 3.1 Introdução aos Logaritmos
- **Definição**: \(\log_a x = y\) se \(a^y = x\).
- **Propriedades**:
  - \(\log_a (xy) = \log_a x + \log_a y\)
  - \(\log_a \left(\frac{x}{y}\right) = \log_a x - \log_a y\)
  - \(\log_a (x^k) = k \log_a x\)
- **Exemplo**: \(\log_2 8 = 3\), pois \(2^3 = 8\).

#### 3.2 Logaritmo Natural
- **Definição**: \(\ln x = \log_e x\), onde \(e \approx 2,71828\).
- **O número \(e\)**: Definido como \(\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n\).

#### 3.3 Resolução de Equações Logarítmicas
- **Exemplo**: \(\ln x + \ln (x + 1) = \ln 6\)
  - \(\ln (x (x + 1)) = \ln 6\)
  - \(x^2 + x = 6\)
  - \(x^2 + x - 6 = 0\)
  - Soluções: \(x = 2\) ou \(x = -3\), mas \(x > 0\), então \(x = 2\).

#### 3.4 Logaritmos e Limites
- **Exemplo**: \(\lim_{x \to 0^+} \ln x = -\infty\).

---

### Módulo 4: Derivadas

#### 4.1 Introdução às Derivadas
- **Definição**: \(f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}\), a inclinação da tangente.
- **Exemplo**: Para \(f(x) = x^2\), \(f'(x) = \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h} = 2x\).

#### 4.2 Regras de Diferenciação
- **Potências**: \(\frac{d}{dx} x^n = n x^{n-1}\)
- **Produto**: \(\frac{d}{dx} [f(x) g(x)] = f'(x) g(x) + f(x) g'(x)\)
- **Quociente**: \(\frac{d}{dx} \left( \frac{f(x)}{g(x)} \right) = \frac{f'(x) g(x) - f(x) g'(x)}{[g(x)]^2}\)
- **Cadeia**: \(\frac{d}{dx} [f(g(x))] = f'(g(x)) \cdot g'(x)\)

#### 4.3 Derivadas de Funções Específicas
- \(\frac{d}{dx} e^x = e^x\)
- \(\frac{d}{dx} \ln x = \frac{1}{x}\)
- \(\frac{d}{dx} \sin x = \cos x\)

#### 4.4 Diferenciação Implícita
- **Exemplo**: \(x^2 + y^2 = 1\)
  - \(2x + 2y \frac{dy}{dx} = 0\)
  - \(\frac{dy}{dx} = -\frac{x}{y}\)

#### 4.5 Aplicações das Derivadas
- **Máximos e mínimos**: \(f'(x) = 0\) para pontos críticos.
- **Exemplo**: \(f(x) = x^3 - 3x\), \(f'(x) = 3x^2 - 3\), pontos críticos em \(x = 1\) e \(x = -1\).

---

### Conexões entre os Módulos
- **Limites e Derivadas**: A derivada é definida como um limite.
- **Logaritmos e Derivadas**: \(\ln x\) surge na derivada de funções exponenciais.
- **Continuidade e Derivadas**: Se \(f\) é derivável em \(a\), ela é contínua em \(a\).

---

### Exercícios Práticos
1. **Limites**: Calcule \(\lim_{x \to 1} \frac{x^2 - 1}{x - 1}\).
2. **Continuidade**: \(f(x) = \frac{x^2 - 4}{x - 2}\) é contínua em \(x = 2\)?
3. **Logaritmos**: Resolva \(\log_3 (x + 2) = 2\).
4. **Derivadas**: Encontre a derivada de \(f(x) = x^2 \ln x\).

---

### Conclusão
Este curso oferece uma base sólida em cálculo, começando com limites, explorando continuidade e logaritmos, e finalizando com derivadas. Cada módulo conecta-se ao próximo, garantindo uma compreensão clara e progressiva. Se precisar de mais detalhes ou ajuda com exercícios, é só avisar!


