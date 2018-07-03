# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

db.define_table('pc',
                Field('user_email', default=auth.user.email if auth.user else None),
                
                Field('personal_CPU', 'text'),
                Field('personal_MOBO', 'text'),
                Field('personal_GPU', 'text'),
                Field('personal_HDD', 'text'),
                Field('personal_PSU', 'text'),
                Field('personal_CASE', 'text'),
                Field('personal_RAM', 'text'),
                )


# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
