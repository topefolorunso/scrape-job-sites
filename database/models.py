from sqlalchemy import TIMESTAMP, Boolean, Column, String, Integer, text
from sqlalchemy.sql import expression
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# class Company(Base):
# 	__tablename__ = 'companies'

# 	id = Column(Integer, primary_key=True)
# 	name = Column(Text, nullable=False)

class Job(Base):

	__tablename__ = 'jobs'

	id 					= Column(Integer, primary_key=True, nullable=False)
	role 				= Column(String, nullable=False)
	experience_level 	= Column(String, nullable=True)
	location 			= Column(String, nullable=False)
	url 				= Column(String, nullable=False, unique=True)
	company 			= Column(String, nullable=False)
	created_at 			= Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("datetime('now')"))
	qualify_for 		= Column(Boolean, nullable=False, server_default=expression.false())
	is_sent 			= Column(Boolean, nullable=False, server_default=expression.false())





