# Sass & Scss

Holberton School – Front-end Web Development  
Project: Sass & Scss  
Author: Florian Chéreau

## Project Overview

This project introduces the fundamentals of **Sass** and **SCSS**, two powerful CSS preprocessors that improve structure, readability, and efficiency in stylesheet development.

The goal of this project is to explore features that regular CSS does not provide natively:
- Variables
- Nested declarations
- Mixins
- Extend/inheritance rules
- File imports
- Flow control directives (`@each`, `@for`, etc.)

Throughout the tasks, you will progressively build SCSS files that demonstrate the strengths of Sass preprocessing while keeping your code clean and maintainable.

## Learning Objectives

By the end of this project, you should be able to explain:

### General
- What Sass means  
- The difference between **Sass** and **SCSS**  
- How to write Sass & SCSS files  
- What preprocessing is and why it is useful  
- How to declare and use **variables**  
- How **nested definitions** work  
- How to **import** external Sass files  
- How to declare and use **mixins**  
- How to apply **extend/inheritance** styles  
- How to manipulate **operators**  
- How to use Sass flow control directives:
  - `@if`
  - `@for`
  - `@each`
  - `@while`

## Resources

You are encouraged to read or watch:
- Sass Basics  
- Sass Flow Control Directives  
- Sass Official Documentation  
- Sass Reference Guide  

These resources introduce the main concepts required in this project.

## Sass Installation

This project uses **Sass 1.82.0+** on Ubuntu 20.04 LTS.

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install -g npm@10
sudo npm install -g sass@^1.82.0
sass --version
```

# Project Structure

## Repository
- GitHub repository: `holbertonschool-web_front_end`
- Directory: `sass_scss`

## Example file structure

sass_scss/
├── 0-debug_log.scss
├── 1-color_variable.scss
├── 2-color_variables.scss
├── 3-nested_tag.scss
├── 4-nested_class.scss
├── 5-nested_child.scss
├── 6-nested_hover.scss
├── 7-nested_deeper.scss
├── 8-mixin_margins.scss
├── 9-extend_list.scss
├── 10-colors.scss
├── 10-import_colors.scss
├── 11-photos.scss
├── 11-loop_photos.scss
├── 12-loop_header.scss
└── README.md

# Requirements

## General
- All files must end with a new line  
- All `.scss` files must begin with a comment describing the task  
- A `README.md` file is mandatory  
- No external CSS frameworks or libraries  
- Sass files must compile successfully using the required version  

## Code Quality
- Keep SCSS files organized  
- Use variables and mixins to avoid repetition  
- Maintain clear and logical nesting  
- Avoid unnecessary selectors  

# Sass Preprocessing: Overview

Sass is a preprocessor that enhances CSS with features like variables, nesting, mixins, inheritance, and programmatic logic.

## Workflow
1. Write `.scss` files  
2. Compile them using Sass  
3. The browser reads the resulting `.css` file  

## Benefits of Sass
- Cleaner and more structured CSS  
- Ability to reuse code through mixins and loops  
- Consistency through variables  
- Reduced duplication via `@extend`  
- Better modularity with imports  

# Key Concepts (Summary)

## Variables
Reusable values for colors, fonts, spacing, etc.

## Nesting
Cleaner hierarchical selectors.

## Mixins
Reusable blocks of CSS with optional parameters.

## Extend / Inheritance
Share common styles between selectors.

## Imports & Modules
Split SCSS into smaller, maintainable files.

## Flow Control
Generate CSS programmatically using:
- `@for`
- `@each`
- `@if`
- `@while`

# Testing and Compilation

To compile SCSS files:

Example:

Always verify:
- Compilation succeeds  
- Output CSS matches the requirements  
- No redundant CSS is generated  

# Author

Name: Florian Chéreau  
GitHub: https://github.com/C-Florian  
Holberton School – France (Sens)
