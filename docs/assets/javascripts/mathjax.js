window.MathJax = {
    loader: {load: ['[tex]/color']},
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true,
      packages: {'[+]': ['color']} // Add cancel extension
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    },
    mml: { forceReparse: true }
  };
  
  document$.subscribe(() => { 
    MathJax.startup.output.clearCache()
    MathJax.typesetClear()
    MathJax.texReset()
    MathJax.typesetPromise()
  })
