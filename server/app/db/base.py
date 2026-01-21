# Import all the models, so that Base has them before being
# imported by Alembic or used by create_all
from .base_class import Base  # noqa
from ..models.models import User, Project  # noqa
# Add any other models here
