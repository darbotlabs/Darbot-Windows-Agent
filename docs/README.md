# Darbot Windows Agent Documentation Site

This directory contains the GitHub Pages site for Darbot Windows Agent.

## 🎨 Design Philosophy

The site features a **Retro Cyber Modern Fluent** design aesthetic:

- **Cyber Grid Background**: Animated grid pattern with neon accents
- **Gradient Colors**: Cyan (#00f0ff), Magenta (#ff00ff), and Green (#00ff88)
- **Typography**: Orbitron (headings), Rajdhani (body), Share Tech Mono (code)
- **Animations**: Smooth transitions, glow effects, and interactive elements
- **Fluent Design**: Modern UI principles with depth and motion

## 📁 Structure

```
docs/
├── index.html              # Main documentation page
├── assets/
│   ├── css/
│   │   └── style.css      # Comprehensive styling
│   └── js/
│       └── main.js         # Interactive features
├── _config.yml             # Jekyll configuration
└── README.md               # This file
```

## 🌟 Features

### Sections

1. **Hero**: Eye-catching introduction with terminal animation
2. **Features**: 6 key capabilities with interactive cards
3. **Architecture**: System design and AutoGen 2.0 integration
4. **Demos**: Video demonstrations with UI grounding examples
5. **Documentation**: Installation, quick start, and usage examples
6. **API Reference**: Complete API documentation and tool reference
7. **FAQ**: Searchable frequently asked questions

### Interactive Elements

- Smooth scrolling navigation
- Mobile-responsive design
- FAQ accordion with search
- Code copy buttons
- Parallax effects
- Typing animations
- Hover glow effects

## 🚀 Local Development

To run locally:

```bash
# Using Python's built-in server
cd docs
python -m http.server 8000

# Or using Node.js
npx http-server docs -p 8000
```

Visit `http://localhost:8000` in your browser.

## 🌐 Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the main branch.

URL: https://darbotlabs.github.io/Darbot-Windows-Agent/

## 📝 Updating Content

### Adding New Sections

1. Add HTML in `index.html`
2. Style in `assets/css/style.css`
3. Add interactivity in `assets/js/main.js`

### Updating Documentation

- Edit code examples in `index.html`
- Update API references in the API section
- Add new FAQ items in the FAQ section

### Customizing Design

- Colors: Edit CSS variables in `:root`
- Fonts: Update Google Fonts import
- Animations: Modify keyframes in CSS

## 🛠️ Technologies

- **HTML5**: Semantic markup
- **CSS3**: Advanced styling with animations
- **JavaScript**: Vanilla JS for interactivity
- **Jekyll**: Static site generation
- **GitHub Pages**: Hosting platform

## 📚 Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages](https://pages.github.com/)
- [Google Fonts](https://fonts.google.com/)

## 🤝 Contributing

Contributions to improve the documentation site are welcome! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - See [LICENSE](../LICENSE) for details.
