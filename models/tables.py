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
                
db.define_table('CPU',
                Field('cpu_name', 'text'),
				Field('cpu_price', 'text'),
                Field('cpu_speed', 'text'),
				Field('cpu_ratings', 'text'),
                Field('cpu_cores', 'text'),
                )
                
db.define_table('motherboard',
                Field('motherboard_name', 'text'),
                Field('motherboard_price', 'text'),
                Field('motherboard_socket', 'text'),
                Field('motherboard_ram','text'),
                Field('motherboard_ratings','text'),
                )
                
db.define_table('memory',
                Field('memory_name', 'text'),
                Field('memory_speed', 'text'),
                Field('memory_price', 'text'),
                Field('memory_size','text'),
                Field('memory_price_gb','text'),
                )
                
db.define_table('GPU',
                Field('GPU_name', 'text'),
                Field('GPU_price', 'text'),
                Field('GPU_memory','text'),
                Field('GPU_chipset', 'text'),
                )
                

                
db.define_table('PSU',
                Field('powersupply_name', 'text'),
                Field('powersupply_watts', 'text'),
                Field('powersupply_price', 'text'),
                Field('powersupply_series','text'),
                Field('powersupply_efficiency','text'),
                )
                
db.define_table('tower',
                Field('tower_name', 'text'),
                Field('tower_price','text'),
                Field('tower_type', 'text'),
                )

                
db.define_table('hdd',
                Field('hdd_name', 'text'),
                Field('hdd_type', 'text'),
                Field('hdd_capacity', 'text'),
                Field('hdd_price','text'),
                Field('hdd_price_gb','text'), #price/gb
                Field('hdd_series','text'),
                )
                



# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
