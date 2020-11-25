from django.urls import path
from rift_valley import views

urlpatterns = [
    path('',views.start_page,name='index'),
    path('',views.page_range_js,name='rangejs'),
    path('',views.page_range_css,name='rangecss'),
    path('',views.page_equation_pic,name='result_pic'),
    path('initial_state/', views.initial_state, name='initial'),
    path('general_info/', views.general_info, name='gm'),
    path('people/', views.people_info, name='people'),
    path('animal/', views.animal_info, name='animal'),
    path('vector_A/', views.vector_A_info, name='vector_A'),
    path('vector_B/', views.vector_B_info, name='vector_B'),
    path('vector_C/', views.vector_C_info, name='vector_C'),
    path('vector_D/', views.vector_D_info, name='vector_D'),
    path('livestock_population/', views.livestock_population, name='livestock_population'),
    path('human_population/', views.human_population, name='human_population'),
    path('human_dalys/', views.human_dalys, name='human_dalys'),
    path('early_detection/', views.early_detection, name='early_detection'),
    path('passive_surveillance/', views.passive_surveillance, name='passive_surveillance'),
    path('active_surveillance/', views.active_surveillance, name='active_surveillance'),
    path('lab_diagnosis/', views.lab_diagnosis, name='lab_diagnosis'),
    path('coord_and_comm/', views.coord_and_comm, name='coord_and_comm'),
    path('movement_control/', views.movement_control, name='movement_control'),
    path('strategic_vaccination/', views.strategic_vaccination, name='strategic_vaccination'),
    path('salary_allowances/', views.salary_allowances, name='salary_allowances'),
    path('capital_costs/', views.capital_costs, name='capital_costs'),
    path('total_annual_cost/', views.total_annual_cost, name='total_annual_cost'),
    path('CBA/', views.CBA, name='CBA'),
    path('sensitivity_analysis/', views.sensitivity_analysis, name='sensitivity_analysis'),
    path('pdftry/', views.generate_view, name='pdftry'),
]