# Modern Software Engineering with DevOps

## Week 1 Porfolio Project Report

### Features
1. User registration and login.
2. Setup "items", "bundles", and "programs" and track changes.
3. Display data in heirarchy (Program --> Bundle --> item) with cross filtering or drilldown based on selection.
4. Issue tracking by program, with assignable tasks.

### API End Points
#### Programs
| Name | Method | Parameter |
|------|--------|-----------|
| Create | POST | /programs |
| index | GET | /programs |
| Show | GET | /programs/{id} |
| Delete | DELETE | /programs/{id} |
| Update | PUT | /programs{id} |

#### Bundles
| Name | Method | Parameter |
|------|--------|-----------|
| Create | POST | /bundles |
| index | GET | /bundles |
| Show | GET | /bundles/{id} |
| Delete | DELETE | /bundles/{id} |
| Update | PUT | /bundles{id} |
| Filter | GET | /bundes/program/{id} |

#### Items
| Name | Method | Parameter |
|------|--------|-----------|
| Create | POST | /items |
| index | GET | /items |
| Show | GET | /items/{id} |
| Delete | DELETE | /items/{id} |
| Update | PUT | /items{id} |
| Filter | GET | /itmes/bundle/{id} |

#### Issues
| Name | Method | Parameter |
|------|--------|-----------|
| Create | POST | /issues |
| index | GET | /issues |
| Show | GET | /issues/{id} |
| Delete | DELETE | /issues/{id} |
| Update | PUT | /issues{id} |
| tasks | GET | /issues/{id}/tasks |

#### Tasks
| Name | Method | Parameter |
|------|--------|-----------|
| Create | POST | /tasks |
| index | GET | /tasks |
| Show | GET | /tasks/{id} |
| Delete | DELETE | /tasks/{id} |
| Update | PUT | /tasks{id} |

#### Users
| Name | Method | Parameter |
|------|--------|-----------|
| Create | POST | /users |
| index | GET | /users |
| Show | GET | /users/{id} |
| Delete | DELETE | /users/{id} |
| Update | PUT | /users{id} |
| Assignments | GET | /users/{id}/assignments|

### DB Schema
Program Management
1. users
    - user_id: pk
    - email
    - first name
    - last name
    - password
2. programs
    - program_id: pk
    - program name
    - program type
    - retailer
    - retailer Item number
    - Program GTIN/UPC
    - season
    - year
3. bundles
    - bundle_id: pk
    - bundle description
    - UPC
4. items
    - item_id: pk
    - item description
    - UPC
    - language
5. issues
    - issue description
    - notes
    - issue create date
    - issue due date
    - program_id
6. tasks
    - task id: pk
    - task description
    - assigned user_id: fk
    - task create date
    - task due date
    - status
    - complete date
7. programs_bundles
    - program_id: pk; fk ref programs
    - bundle_id: pk; fk ref bundles
    - bundle qty
8. bundles_itmes
    - bundle_id: pk; fk ref bundles
    - item_id: pk; fk ref items
    - item qty