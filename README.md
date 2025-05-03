# Verity

## Budget | Forecast | Financial Plan

### Initial Goals and MVP

Quick overview of MVP:
(MVP completion will be considered the 0.1.0 Release, untill then we are Alpha and sprint counting.)

1. Local First to ensure security, it is your finances at the end of the day
1. Stored in a local pylimbo database (sqlite in rust)
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
  * **Limbo:** database - sqlite replacement.
  * **Ruff:**  code formatter.
  * **UV:**  Package management and virtual environment handler.
* **Database:** Limbo. Chosen for the previous Rust constraint and also performance
* **Security Focus:**
  * Input validation on all user inputs.
  * Local first development ideal, Later we can add self host capability.
  *
* **Performance:**  Optimization strategies will be implemented throughout the development process (e.g., efficient database queries, caching).
* **Dependency Management:** All external dependencies will be meticulously managed using UV.

## Acceptance Criteria

### To be concidered a MVP success we must achieve;

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
