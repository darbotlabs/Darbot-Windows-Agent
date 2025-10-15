# Contributing to Darbot Documentation

Thank you for your interest in improving the Darbot Windows Agent documentation! This guide will help you contribute effectively.

## 📋 Documentation Structure

```
docs/
├── index.html              # Main documentation page
├── assets/
│   ├── css/
│   │   └── style.css      # All styling (cyber theme)
│   └── js/
│       └── main.js         # Interactive features
├── _config.yml             # Jekyll configuration
├── README.md               # Documentation overview
├── ENHANCEMENTS.md         # Technical improvements guide
└── CONTRIBUTING.md         # This file
```

## 🎨 Design Guidelines

### Color Palette

The site uses a **Retro Cyber Modern Fluent** aesthetic:

```css
--cyber-primary: #00f0ff;     /* Cyan - primary accents */
--cyber-secondary: #ff00ff;   /* Magenta - secondary accents */
--cyber-accent: #00ff88;      /* Green - highlights */
--cyber-warning: #ffaa00;     /* Orange - warnings */
--cyber-dark: #0a0e27;        /* Dark background */
--cyber-darker: #050814;      /* Darker background */
```

### Typography

- **Headings**: Orbitron (bold, futuristic)
- **Body Text**: Rajdhani (clean, readable)
- **Code**: Share Tech Mono (monospace)

### Animation Principles

- Smooth transitions (0.3s ease)
- Subtle glow effects on hover
- Parallax scrolling for depth
- Typing animations for terminals

## 📝 Content Guidelines

### Writing Style

1. **Clear and Concise**: Use simple language
2. **Action-Oriented**: Start with verbs (Install, Configure, Run)
3. **Examples First**: Show code before explaining
4. **Consistent Tone**: Professional but friendly

### Code Examples

Always include:
- Syntax highlighting
- Copy button functionality
- Comments for complex logic
- Complete, runnable examples

Example:
```html
<pre class="code-block"><code>from darbot_windows_agent.agent import Agent

# Initialize agent with Google Gemini
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
agent = Agent(llm=llm)</code></pre>
```

### Screenshots and Media

- Use descriptive alt text
- Optimize images (WebP preferred)
- Include captions
- Link to full resolution versions

## 🛠️ Making Changes

### Quick Edits

For small changes (typos, wording):

1. Edit directly on GitHub
2. Create a pull request
3. Describe your changes

### Major Changes

For significant updates:

1. **Fork the repository**
   ```bash
   gh repo fork darbotlabs/Darbot-Windows-Agent
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Darbot-Windows-Agent.git
   cd Darbot-Windows-Agent
   ```

3. **Create a branch**
   ```bash
   git checkout -b docs/your-improvement
   ```

4. **Make your changes**
   - Edit `docs/index.html` for content
   - Edit `docs/assets/css/style.css` for styling
   - Edit `docs/assets/js/main.js` for interactivity

5. **Test locally**
   ```bash
   cd docs
   python -m http.server 8000
   # Visit http://localhost:8000
   ```

6. **Commit and push**
   ```bash
   git add docs/
   git commit -m "docs: improve XYZ section"
   git push origin docs/your-improvement
   ```

7. **Create pull request**
   - Go to GitHub
   - Click "New Pull Request"
   - Describe your changes
   - Link related issues

## 📚 Content Areas

### Priority Improvements

We especially welcome contributions in these areas:

1. **More Examples**
   - Real-world use cases
   - Integration patterns
   - Troubleshooting scenarios

2. **Video Content**
   - Tutorial videos
   - Demo recordings
   - Walkthrough guides

3. **API Documentation**
   - Method descriptions
   - Parameter explanations
   - Return value details

4. **FAQ Expansion**
   - Common questions
   - Error messages
   - Best practices

### Adding New Sections

To add a new major section:

1. **HTML Structure**
   ```html
   <section class="your-section" id="your-section">
       <div class="container">
           <div class="section-header">
               <h2 class="section-title">
                   <span class="section-icon">🎯</span>
                   Your Section Title
               </h2>
               <p class="section-subtitle">Brief description</p>
           </div>
           <!-- Your content here -->
       </div>
   </section>
   ```

2. **CSS Styling**
   ```css
   .your-section {
       padding: 6rem 0;
       background: rgba(26, 31, 58, 0.3);
   }
   ```

3. **Navigation Link**
   ```html
   <li><a href="#your-section" class="nav-link">Your Section</a></li>
   ```

## 🎯 Interactive Features

### Adding Copy Buttons

For code blocks:

```html
<div class="code-block-container">
    <div class="code-block-header">
        <span class="code-block-lang">python</span>
        <button class="copy-btn" data-clipboard-text="your code here">
            Copy
        </button>
    </div>
    <pre class="code-block"><code>your code here</code></pre>
</div>
```

### Adding FAQ Items

```html
<div class="faq-item">
    <button class="faq-question">
        <span>Your question here?</span>
        <svg class="faq-icon"><!-- chevron icon --></svg>
    </button>
    <div class="faq-answer">
        <p>Your detailed answer here</p>
    </div>
</div>
```

## 🧪 Testing Checklist

Before submitting:

- [ ] Test on Chrome, Firefox, Safari
- [ ] Test on mobile devices
- [ ] Verify all links work
- [ ] Check for typos and grammar
- [ ] Validate HTML structure
- [ ] Test JavaScript functionality
- [ ] Check responsive breakpoints
- [ ] Verify accessibility (ARIA labels)

## 🌐 Accessibility

Ensure your contributions are accessible:

1. **Semantic HTML**: Use proper tags (`<nav>`, `<section>`, `<article>`)
2. **Alt Text**: Describe all images
3. **Keyboard Navigation**: All interactive elements accessible via keyboard
4. **Color Contrast**: Maintain WCAG AA standards
5. **ARIA Labels**: Add where semantic HTML insufficient

Example:
```html
<button aria-label="Copy code to clipboard" class="copy-btn">
    Copy
</button>
```

## 📱 Responsive Design

Test at these breakpoints:

- **Mobile**: 320px - 767px
- **Tablet**: 768px - 1023px
- **Desktop**: 1024px - 1439px
- **Large Desktop**: 1440px+

## 🔍 SEO Best Practices

- Use descriptive `<title>` tags
- Include `<meta>` descriptions
- Use proper heading hierarchy (h1 → h2 → h3)
- Add `alt` text to images
- Create descriptive URLs/anchors

## 📄 License

All documentation contributions are released under the MIT License.

## 🤝 Getting Help

- **Questions**: Open a [Discussion](https://github.com/darbotlabs/Darbot-Windows-Agent/discussions)
- **Bugs**: Open an [Issue](https://github.com/darbotlabs/Darbot-Windows-Agent/issues)
- **Chat**: Join our community channels

## 🎉 Recognition

Contributors are recognized in:
- README.md contributors section
- Release notes
- Documentation credits page

Thank you for helping improve Darbot documentation! 🚀
