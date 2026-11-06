# DEVLOG

## July 25, 2026 - Draft

**Feature:** Filter Books by Author Name

**Changes Made:**
1. **Added Author Column:** 
   - Updated `models.py` to include the `author` column in the `Book` model.
   - Configured it as a `String` and `nullable=False`. 
   - Added a `server_default` so any existing books without an author won't break the database.
   - Added inline comments for learning purposes.

## July 27, 2026 - Draft

**Feature:** Filter Books by Author Name (Steps 2 & 3)

**Changes Made:**
1. **Updated Schemas:**
   - Modified `schemas.py` to include the `author` field in the `BookBase` schema.
   - Added validation via Pydantic's `Field` and included inline comments.
2. **Database Migration Instructions:**
   - Provided the raw SQL command to safely add the `author` column to the PostgreSQL `books` table using `ALTER TABLE`.
3. **Database Relationships Update:**
   - Updated `Vote` model in `models.py` to include `ondelete="CASCADE"` for both `user_id` and `book_id` foreign keys, ensuring votes are automatically removed when a related user or book is deleted.
4. **Code Cleanup:**
   - Removed redundant comments across `main.py`, `oauth2.py`, `routers/books.py`, and `routers/user.py`.
5. **Get Books API Update:**
   - Modified `get_books` in `routers/books.py` to accept an optional `author` query parameter.
   - Built the query conditionally: if `author` is provided, it filters books using SQLAlchemy's `.filter().contains()`.
   - Delayed executing the query with `.all()` until the very end.
   - Added descriptive comments for every line of code inside the function to explain the logic.
6. **Pydantic V2 Migration:**
   - Updated `schemas.py` by replacing `orm_mode = True` with `from_attributes = True` inside the `Book_with_votes` config to ensure compatibility with Pydantic V2.
7. **Endpoint Testing:**
   - Successfully tested both the `Create Book` (POST) and `Get Books` (GET) endpoints (including the new author filtering capabilities) to ensure proper database operations and correct response models.

## November 6, 2026 - Bug Fixes & Security Hardening

**Feature:** Endpoint Security & Error Handling

**Bugs Identified:**
1. **Unprotected Book Operations:** `POST`, `PUT`, and `DELETE` endpoints under `/books` were publicly accessible without requiring JWT authentication.
2. **Unhandled User Lookup in Auth Guard:** In `oauth2.py`, if a user was deleted from the database while holding a valid JWT, `get_current_user` returned `None`, causing a 500 server crash when reading `current_user.id`.
3. **Duplicate Email Crash:** Registering an existing email triggered an unhandled PostgreSQL unique constraint violation (500 Internal Server Error).
4. **Stale Virtual Environment Paths:** Hardcoded directory paths in `venv/bin/` caused `uvicorn` and `pip` command failures.

**Changes Made:**
1. **Protected Book Mutating Routes:**
   - Injected `current_user: models.User = Depends(oauth2.get_current_user)` into `create_book`, `update_book`, and `delete_book` in `routers/books.py`.
   - Kept `GET /books/` and `GET /books/{id}` public for unauthenticated browsing.
2. **Hardened Auth Dependency:**
   - Added `if user is None: raise credentials_exception` in `oauth2.py` to convert unexpected user states into clean 401 Unauthorized errors.
3. **Added Duplicate Email Validation:**
   - Added a database query check in `routers/user.py` before `db.add()` to return a clean 409 Conflict if an email is already in use.
4. **Repaired Virtual Environment:**
   - Updated executable shebangs in `venv/bin/` so `uvicorn` and `pip` execute properly.