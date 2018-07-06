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
                )
                
db.define_table('cpu',
                Field('cpu_name', 'text'),
                Field('cpu_speed', 'text'),
                Field('cpu_chipset', 'text'),
                )
                
db.define_table('gpu',
                Field('gpu_name', 'text'),
                Field('gpu_speed', 'text'),
                Field('gpu_chipset', 'text'),
                )
                
db.define_table('mem',
                Field('mem_name', 'text'),
                Field('mem_speed', 'text'),
                Field('mem_chipset', 'text'),
                )
                
db.define_table('psu',
                Field('psu_name', 'text'),
                Field('psu_wattage', 'text'),
                Field('psu_rating', 'text'),
                )
                
db.define_table('mobo',
                Field('mobo_name', 'text'),
                Field('mobo_size', 'text'),
                Field('mobo_socket', 'text'),
                )
                
db.define_table('hdd',
                Field('hdd_name', 'text'),
                Field('hdd_type', 'text'),
                Field('hdd_size', 'text'),
                )
                
db.define_table('tower',
                Field('tower_name', 'text'),
                Field('tower_size', 'text'),
                )


# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
