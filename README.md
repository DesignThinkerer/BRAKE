# BRAKE
![Project Status: Work in Progress](https://img.shields.io/badge/Project%20Status-Work%20in%20Progress-yellow)

**Belgian Road Automated Knowledge Engine**  

BRAKE is a Python-powered tool that simplifies the process of learning the Belgian road code. By leveraging web scraping and TiddlyWiki integration, BRAKE automatically generates tiddlywiki-compatible flashcards to help learners study efficiently and retain information effectively.

## 🚀 Features  
- **Automated Flashcard Creation**: Scrapes the official Belgian road code to generate flashcards for quick and effective learning.  
- **TiddlyWiki Integration**: Exports flashcards directly into TiddlyWiki for easy access and customization.  
- **Customizable Content**: Tailor flashcards to focus on specific categories or rules.  
- **Efficient Workflow**: Save hours of manual work with automated processing and organization.  

## 🔧 Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/brake.git
   cd brake
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## 📋 Usage

We provide multiple options to get started:

1. **Ready-to-Use TiddlyWiki**  
   - [Download the Ready-to-Use TiddlyWiki](https://github.com/DesignThinkerer/BRAKE/releases/latest/download/BRAKE_TiddlyWiki.html)
   - Open it in your browser and save locally after editing.  

2. **Create Your Own Wiki on Tiddlyhost**  
   Want a hosted solution? Use our template on Tiddlyhost to get started immediately:  
   - [Get Your Own Wiki on Tiddlyhost](https://tiddlyhost.com/?template=BRAKE_Template)  

3. **Import the Flashcards as a Plugin**  
   Already have a TiddlyWiki?  
   - [Download the flashcard plugin](https://github.com/DesignThinkerer/BRAKE/releases/latest/download/BRAKE_Flashcards_Plugin.json)


If you'd like to customize the flashcards or generate them from scratch, follow the instructions below.

1. Launch the script and follow the prompts to scrape the Belgian road code.
2. Customize flashcards as needed using the built-in options.
3. Export the generated flashcards to a TiddlyWiki file for easy access and study.

## 📂 Directory Structure
   ```graphql
   BRAKE/
   │
   ├── data/                 # Raw scraped data  
   ├── flashcards/           # Generated flashcards  
   ├── tiddlywiki/           # Exported TiddlyWiki files  
   ├── scripts/              # Helper scripts for scraping and processing  
   ├── main.py               # Main application entry point  
   ├── requirements.txt      # Python dependencies  
   └── README.md             # Project documentation
   ```

## 🌱 Roadmap
- Add support for other languages or regional road codes.
- Include a GUI for non-technical users.
- Enhance flashcard customization options.
- Integrate with other flashcard tools (e.g., Anki).

## 🤝 Contributing
We welcome contributions! Here's how you can get involved:

1. Fork the repo.
2. Create a branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch and open a pull request:
   ```bash
   git push origin feature-name
   ```
   
## 🛠️ Built With
Python for scripting and automation.
BeautifulSoup for web scraping.
TiddlyWiki for flashcard storage and study.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 💬 Contact
Have questions or suggestions? Feel free to reach out:

- Author: Théophile Desmedt
- Email: hello@theophile.dev
<!-- - Portfolio: https://theophile.dev/portfolio -->
