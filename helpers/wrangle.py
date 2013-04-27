import pandas as pd
import csv

dise = pd.read_csv('dise_facility_enrol.csv')
grouped = dise.groupby('district')

fieldnames = ['district', 'classrooms', 'blackboards', 'playgrounds',
'toilets_common', 'toilets_boys', 'toilets_girls',
'libraries', 'books', 'computers', 'electricity_y',
'electricity_n', 'electricity_non', 'students', 'boys', 'girls',
'classrooms_repair', 'headmaster_rooms', 'teachers_male', 'teachers_female']

file = open('aggregated.csv', 'w')
writer = csv.DictWriter(file, fieldnames)
writer.writeheader()

for name, group in grouped:

        data = {'district':'', 'classrooms':'', 'blackboards':'', 'playgrounds':'',
        'toilets_common':'', 'toilets_boys':'', 'toilets_girls':'',
        'libraries':'', 'books':'', 'computers':'', 'electricity_y':'',
        'electricity_n':'', 'electricity_non':'', 'students':'', 'boys':'', 'girls':'',
        'classrooms_repair':'', 'headmaster_rooms':'', 'teachers_male':'', 'teachers_female':''}

        data['district']= name
        print name
        data['classrooms']= sum(group.tot_clrooms)
        data['blackboards']= sum(group.blackboard)
        playgrounds = 0
        for ground in group.playground:
                if ground == 1:
                        playgrounds = playgrounds + 1
        data['playgrounds']= (playgrounds)
        data['toilets_common']= sum(group.toilet_common)
        data['toilets_boys']= sum(group.toilet_boys)
        data['toilets_girls']= sum(group.toilet_girls)
        libraries = 0
        for library in group.library_yn:
                if library == 1:
                        libraries = libraries + 1
        data['libraries']= (libraries)
        data['books']= sum(group.books_in_library)
        electricity_y, electricity_n, electricity_non = 0, 0, 0
        for elec in group.electricity:
                if elec == 1:
                        electricity_y = electricity_y + 1
                elif elec == 2:
                        electricity_n = electricity_n + 1
                else:
                        electricity_non = electricity_non + 1
        data['electricity_y']= electricity_y
        data['electricity_n']= electricity_n
        data['electricity_non']= electricity_non
        boys = (sum(group.class1_total_enr_boys) + sum(group.class2_total_enr_boys) +
                        sum(group.class3_total_enr_boys) + sum(group.class4_total_enr_boys) +
                        sum(group.class5_total_enr_boys) + sum(group.class6_total_enr_boys) +
                        sum(group.class7_total_enr_boys) + sum(group.class8_total_enr_boys))

        girls = (sum(group.class1_total_enr_girls) + sum(group.class2_total_enr_girls) +
                        sum(group.class3_total_enr_girls) + sum(group.class4_total_enr_girls) +
                        sum(group.class5_total_enr_girls) + sum(group.class6_total_enr_girls) +
                        sum(group.class7_total_enr_girls) + sum(group.class8_total_enr_girl))

        data['boys']= boys
        data['girls']= girls
        data['students']= boys+girls
        data['classrooms_repair']= sum(group.classrooms_require_major_repair)
        data['headmaster_rooms']= sum(group.separate_room_for_headmaster)
        data['computers'] = sum(group.no_of_computers)
        data['teachers_male']= sum(group.male_tch)
        data['teachers_female']= sum(group.female_tch)
        writer.writerow(data)