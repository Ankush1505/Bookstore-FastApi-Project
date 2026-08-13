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