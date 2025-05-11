# Verity

## Budget | Forecast | Financial Plan

### A Web based application to allow you to input financial transactions, in turn allowing you to budget, forecast and plan your money.

### Initial Goals and MVP

Quick overview of MVP:

(MVP completion will be considered the 0.1.0 Release, untill then we are Alpha and sprint counting.)

1. Local First to ensure security, it is your finances at the end of the day
1. ~~Stored in a local pylimbo database (sqlite in rust)~~
1. Stored in a local sqlite database
1. Easily distributable. any PC should be able to clone and run with no extra steps.
1. Docker later, not part of MVP but should build with the plan to dockerise
1. Test driven development - each class / method should have unit testing and integration testing.
1. Features to have for MVP (more info in [Acceptance Criteria](#Acceptance-Criteria))
  - Add basic accounts
  - Add Categories and Sub-Categories (3 tier hierarchy max)
  - Assign spending money to each Category
  - Add transactions from and to accounts (with Category assigned)
  - Simple Reporting

## Constraints

* **Rust-First Tooling:**  Where possible, we will leverage Rust-built tools for development, testing, and build processes.  This includes, but is not limited to:
  ~~* **Limbo:** database - sqlite replacement.~~
  * **Ruff:**  code formatter.
  * **UV:**  Package management and virtual environment handler.
  * **Pydantic:** Data Validation Tool
* **Database:** ~~Limbo. Chosen for the previous Rust constraint and also performance~~
* **Security Focus:**
  * Input validation on all user inputs.
  * Local first development ideal, Later we can add self host capability.
  *
* **Performance:**  Optimization strategies will be implemented throughout the development process (e.g., efficient database queries, caching).
* **Dependency Management:** All external dependencies will be meticulously managed using UV.

## Acceptance Criteria

### To be considered a MVP success we must achieve;

* [ ] **High Test Coverage (80% +)**
* [ ] **Budget Creation:**
  * [ ] Ability to create a new budget and have multiple separate budgets
  * [ ] Ability to have up to a 3 Tier nested Hierarchy of Categories for spending.
  * [ ] Ability to have multiple accounts on the budget, with different account types (mostly simple though, no interest tracking)
* [ ] **Expense Tracking:**
  * [ ] Ability to add new expenses with descriptions and amounts.
  * [ ] Ability to categorise expenses.
  * [ ] Manual input of expenses.
* [ ] **Reporting:**
  * [ ] Display a simple monthly summary of income and expenses.
  * [ ] Report should be visually clear (e.g., charts, tables).
  * [ ] At or Above the Level of reporting in [DPFY](https://github.com/Jake-Pullen/data_pipeline_for_YNAB/)
* [ ] **Data Storage (Initial):**
  * [ ] Database schema defined and implemented.
  * [ ] Basic CRUD operations (Create, Read, Update, Delete) for budget and expense data.
  * [ ] Data validation in the database.
* [ ] **Security:**
  * [ ] HTTPS enabled and configured.
  * [ ] Input validation implemented for all user inputs.
  * [ ] Basic security testing performed (e.g., SQL injection prevention).
* [ ] **UI/UX:**
  * [ ] Responsive Design - Basic responsiveness for common screen sizes.
  * [ ] Clear and concise user interface.

## Future Considerations (Beyond MVP)

* Advanced Reporting (e.g., forecasting, scenario planning)
* Integration with financial institutions (API integration - *this is a significant undertaking & Security Challenge*)
* More sophisticated Account types (e.g., interest calculating credit & debt accounts)
* Mobile application development.
* Investment tracking and analysis.
* Containerisation via Docker for easier more efficient distribution
* Self-Hosting capable for access on devices outside of own network

## Contribution Guidelines

### Ensure you have [uv installed](https://docs.astral.sh/uv/getting-started/installation/)

1. **Fork the Repository:** Create your own fork of the Verity project repository.
1. **Create a Branch:**  Create a new branch for your changes (e.g., `feature/new-feature`, `fix/bug-name`).
1. **Run uv sync** To ensure dependancies are installed and you are ready to go
1. **Follow Code Style:**  Please adhere to our coding standards (We are using Ruff)
1. **Write Clear Commit Messages:**  Use descriptive commit messages to explain the purpose of your changes.
1. **Test Thoroughly:**  Ensure your changes are well-tested, including adding new tests where appropriate.  *Especially remember to add the new tests in `src/tests/test_*.py`.*
1. **Submit a Pull Request:** Once you’ve finished your work, submit a pull request to the stage branch in the Verity project repository.  We’ll review your changes and provide feedback.
