// Renders the maths on every page, including after instant navigation.
document$.subscribe(({ body }) => {
  renderMathInElement(body, {
    // Only the delimiters pymdownx.arithmatex emits. A bare "$" is NOT a delimiter here: the
    // articles quote prices like $20,702, and treating those as maths swallowed the text between them.
    delimiters: [
      { left: "\\(", right: "\\)", display: false },
      { left: "\\[", right: "\\]", display: true },
    ],
  });
});
