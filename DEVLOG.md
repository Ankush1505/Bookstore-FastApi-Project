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