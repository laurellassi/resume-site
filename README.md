# Hosting My Resume Online


### Getting Started

---

This README provides step-by-step instructions for hosting your resume as a static website using **GitHub Pages** and the **Pelican static site generator**. It is designed for developers, students, or anyone looking to showcase their resume online in a simple and efficient way. This project applies principles from **Andrew Etter’s *Modern Technical Writing***, including the use of lightweight markup languages, static site generators, and version control systems.

#### Prerequisites

Requirements in order for you to host and publish your resume online:

1. **GitHub Account:**

    - Create a GitHub account, if you dont already have one: [GitHub sign up](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home).

2. **Install Git:**

    - Download and install Git for Windows: [Git for Windows](https://git-scm.com/downloads/win).

3. **Install Python:**

    - Download and install Python for Windows: [Python for Windows](https://www.python.org/).

4. **Install Pelican with Markdown Support:**

    - Install by running the following command in your windows terminal:
        
        ```bash
        python -m pip install "pelican[markdown]"
        ```

5. **Install a Text Editor:**
    
    - Download and install Visual Studio Code for Windows: [VS Code for Windows](https://code.visualstudio.com/docs/?dv=win64user).

### Setting Up Your Pelican Project

---

1. **Create a Project Folder:**

    - Open your terminal and create a new folder for your project by running the following commands:
        
        ```bash
        mkdir my-resume-site
        cd my-resume-site
        ```

2. **Initialize a Pelican Project:**

    - Run the following command while inside your *my-resume-site* folder to set up a new Pelican site:

        ```bash
        pelican-quickstart
        ```

    Follow the prompts to configure your site. For most options, you can accept the defaults by pressing **ENTER**, but *make sure* to specify the following:
        
    2. What will be the title of this web site?

            Insert the name of your website.

    3. Who will be the author of this web site?
            
            Insert the name of the author.
            
    4. Do you want to specify a URL prefix?
             
            Insert n.
    
    5. What is your time zone?

            Insert your time zone (e.g., America/Winnipeg)

### Creating the Resume in Markdown

---

1. **Open Your Project Folder in VS Code:**

    1. Open VS Code and select **File** in the menu bar.
    2. Click **Open Folder**.
    3. Find your project folder and open it.

2. **Create a New Markdown File:**

    1. In the file explorer right-click on the **content/** folder.  
    2. Select **New File**.
    3. Name the file *resume\.md*

3. **Write Your Resume in Markdown:**

    1. Add the following Metadata at the top of your resume:  
    <br>
        >Title: Resume 
        >Slug: resume
        >Date: [year-month-day]
        >Category: Resume
    
    2. Format your resume.

    3. Save the changes.

**Why Use Markdown?**  
As Andrew Etter explains in *Modern Technical Writing*, lightweight markup languages like Markdown are ideal for technical writing because they are simple, readable, and easy to maintain. By using Markdown, you can focus on the content of your resume without worrying about complex formatting.

### Building the Site

---

1. **Open the terminal in VS Code:**

    - In VS Code, open the integrated terminal by going to **View** > **Terminal**.

2. **Generate the Static Site:**

    - Run the following command in the terminal while inside your project directory to build the site:

        ```bash
        pelican content
        ```

3. **Previewing the Site Locally:**

    1. Run the following command in the terminal to start a local server:
        
        ```bash
        pelican --listen
        ```
    
    2. Open your browser and navigate to:

        `http://localhost:8000`

**Why Use a Static Site Generator?**  
As Andrew Etter explains in *Modern Technical Writing*, static site generators are a great way of hosting a website. They are fast, simple, portable and secure. In particular, Pelican automates the process of converting Markdown into HTML, ensuring a clean and efficient workflow for hosting your resume online.

### Publishing to GitHub Pages

---

1. **Prepare Your Repository:**

    1. Run the following command in the terminal to initialize Git:

        ```bash
        git init
        ```

    2. Create a GitHub repository: [Creating GitHub Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories).

    3. Run the following command in the terminal to connect your local repository to GitHub:

        ```bash
        git remote add origin https://github.com/your-username/your-username.github.io.git
        ```
        *Change* "your-username" to match yours.

2. **Push Source Files to the `main` Branch:**

    1. Stage and commit your source files (everything except the `output/` folder):

        ```bash
        git add .
        git commit -m "Initial commit with source files"
        ```

    2. Push your source files to the `main` branch:

        ```bash
        git push -u origin main
        ```

3. **Generate and Push Static Files to the `gh-pages` Branch:**

    1. Build your static site:

        ```bash
        pelican content
        ```

    2. Navigate to the `output/` folder:

        ```bash
        cd output
        ```

    3. Initialize a new Git repository in the `output/` folder:

        ```bash
        git init
        ```

    4. Create and switch to the `gh-pages` branch:

        ```bash
        git checkout -b gh-pages
        ```

    5. Stage and commit the static files:

        ```bash
        git add .
        git commit -m "Deploy static site to gh-pages"
        ```

    6. Add the remote repository URL (same as before):

        ```bash
        git remote add origin https://github.com/your-username/your-username.github.io.git
        ```

    7. Force push the static files to the `gh-pages` branch:

        ```bash
        git push -u origin gh-pages --force
        ```

4. **Enable GitHub Pages:**

    1. Go to your repository’s settings on GitHub.

    2. Navigate to the **Pages** section.

    3. Set the source branch to `gh-pages` and the folder to `/ (root)`.

5. **Access Your Live Resume:**

    - Your resume will be live at:  
        ```
        https://your-username.github.io
        ```

**Why Git?**  
As Andrew Etter emphasizes in *Modern Technical Writing*, version control systems like Git are essential for collaboration and tracking changes in technical documentation. By using Git, you can easily manage updates to your resume and collaborate with others.

**Why GitHub Pages?**  
Andrew Etter recommends hosting documentation on platforms like GitHub Pages because they integrate seamlessly with version control and static site generators. GitHub Pages provides a free, reliable, and easy-to-use platform for hosting static websites like your resume.

### Further Resources

---

Here are some additional resources to help you learn more about the tools and concepts used in this project:

**Markdown:**

- [Markdown Basic Syntax](https://www.markdownguide.org/basic-syntax/)

**Git and GitHub:**

  - [GitHub Docs](https://docs.github.com/en)
  - [GitHub Pages Guide](https://docs.github.com/en/pages)

**Pelican:**

  - [Pelican Themes](https://github.com/getpelican/pelican-themes)

### FAQs

---

1. **Why is GitHub Pages a good choice for hosting my resume?**
GitHub Pages is an excellent choice because it’s free, user-friendly, and integrates seamlessly with Git. It’s specifically designed for hosting static websites, making it ideal for your resumes, portfolios, and documentation.

2. **Why do I need two branches (`main` and `gh-pages`) for GitHub Pages?**
The `main` branch stores your source files, while the `gh-pages` branch stores the generated static site files. This separation keeps your project organized.

### Credits

---

I'd like too say thank you to,

- Lucas Berzuk
- Arshinder Sidhu

For their help and criticism during the reviewing stage. 

 











