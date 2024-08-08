from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'j4828df73udfa_index'  # Replace with the actual revision ID generated
down_revision = 'e2e999c065cd'  # This should be the ID of your previous migration
branch_labels = None
depends_on = None

def upgrade():
    # Ensure the table and indexes exist as expected
    # Create indexes if they do not exist
    op.create_index('idx_foods_title', 'foods', ['title'], unique=False)
    op.create_index('idx_foods_category', 'foods', ['category'], unique=False)

def downgrade():
    # Drop the indexes if you need to roll back the migration
    op.drop_index('idx_foods_title', table_name='foods')
    op.drop_index('idx_foods_category', table_name='foods')
