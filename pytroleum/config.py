import copy

inputs={
    'curves': {
            'oil': {
                    'Qi_monthly': 19400,
                    'Qf_monthly': 15,
                    'nominal_decline_annual': 1.66073,
                    'b_factor': 1.25,
                    'Dmin_annual': 0.06,
                    'EUR': 789000,
                    },
            'gas':{
                    'Qi_monthly': 111000,
                    'Qf_monthly': 0,
                    'nominal_decline_annual': .64,
                    'b_factor': 1.0,
                    'Dmin_annual': 0.05,
                    'EUR': 6581000,
                    },
            'ngl':{},
        },
    'taxes':{
            'ad_valorum': .025,
            'severance': {
                            'oil': 0.046,
                            'gas':.075,
                        }

            },
    'expenses': {
            'fixed': 10000,
            'variable': {
                        'oil': .03,
                        'gas':0.0,
                        'ngl':0.0,
            },
    },
    'capital':{
            'idc': 3.5*10**6,
            'icc': 3.0*10**6,
            'land':5.0*10**5,
    },
    'max_life_years': 50,
    'production_delay': 3,
    'production_start_date': '20160601',
    'capital_start_date': '20160401',
    'standard_days_in_month': 30.4375,
    'standard_days_in_year': 365.25,
    'price_type': 'flat',
    'price_oil_strip': {'5/1/2019': 53.539999999999999, '5/1/2018': 52.18, '5/1/2017': 51.280000000000001, '06/01/2022': 57.369999999999997, '06/01/2024': 58.75, '05/01/2024': 58.75, '05/01/2022': 57.369999999999997, '05/01/2023': 58.18, '8/1/2021': 56.439999999999998, '8/1/2020': 55.219999999999999, '11/1/2019': 54.25, '11/1/2018': 52.93, '11/1/2020': 55.590000000000003, '11/1/2021': 56.770000000000003, '06/01/2023': 58.18, '3/1/2019': 53.32, '3/1/2018': 52.009999999999998, '2/1/2021': 55.899999999999999, '2/1/2020': 54.600000000000001, '3/1/2017': 51.090000000000003, '8/1/2018': 52.490000000000002, '8/1/2019': 53.82, '8/1/2016': 49.329999999999998, '8/1/2017': 51.469999999999999, '08/01/2024': 58.909999999999997, '08/01/2023': 58.579999999999998, '08/01/2022': 57.770000000000003, '9/1/2019': 53.950000000000003, '9/1/2018': 52.619999999999997, '9/1/2017': 51.530000000000001, '9/1/2016': 49.759999999999998, '6/1/2021': 56.380000000000003, '6/1/2020': 55.130000000000003, '3/1/2020': 54.710000000000001, '3/1/2021': 55.990000000000002, '11/01/2024': 58.909999999999997, '11/01/2023': 58.579999999999998, '11/01/2022': 57.770000000000003, '12/1/2018': 53.07, '12/1/2019': 54.420000000000002, '4/1/2021': 56.100000000000001, '4/1/2020': 54.829999999999998, '01/01/2022': 57.369999999999997, '01/01/2023': 58.18, '01/01/2024': 58.75, '7/1/2017': 51.420000000000002, '7/1/2016': 48.859999999999999, '1/1/2017': 50.850000000000001, '11/1/2017': 51.719999999999999, '11/1/2016': 50.390000000000001, '12/1/2021': 56.93, '12/1/2020': 55.770000000000003, '7/1/2019': 53.729999999999997, '7/1/2018': 52.380000000000003, '03/01/2022': 57.369999999999997, '03/01/2023': 58.18, '03/01/2024': 58.75, '4/1/2017': 51.189999999999998, '1/1/2020': 54.5, '1/1/2021': 55.829999999999998, '4/1/2018': 52.090000000000003, '4/1/2019': 53.420000000000002, '07/01/2024': 58.909999999999997, '07/01/2022': 57.770000000000003, '07/01/2023': 58.579999999999998, '9/1/2020': 55.32, '9/1/2021': 56.520000000000003, '04/01/2023': 58.18, '04/01/2022': 57.369999999999997, '04/01/2024': 58.75, '5/1/2020': 54.969999999999999, '5/1/2021': 56.229999999999997, '10/1/2018': 52.770000000000003, '10/1/2019': 54.090000000000003, '10/1/2016': 50.090000000000003, '10/1/2017': 51.609999999999999, '2/1/2017': 50.979999999999997, '2/1/2018': 51.939999999999998, '2/1/2019': 53.210000000000001, '12/01/2022': 57.770000000000003, '12/01/2023': 58.579999999999998, '12/01/2024': 58.909999999999997, '7/1/2020': 55.159999999999997, '7/1/2021': 56.390000000000001, '10/1/2021': 56.630000000000003, '10/1/2020': 55.439999999999998, '6/1/2018': 52.299999999999997, '6/1/2019': 53.68, '12/1/2016': 50.649999999999999, '12/1/2017': 51.840000000000003, '09/01/2022': 57.770000000000003, '09/01/2023': 58.579999999999998, '6/1/2017': 51.369999999999997, '09/01/2024': 58.909999999999997, '02/01/2024': 58.75, '10/01/2022': 57.770000000000003, '10/01/2023': 58.579999999999998, '10/01/2024': 58.909999999999997, '02/01/2023': 58.18, '02/01/2022': 57.369999999999997, '1/1/2019': 53.140000000000001, '1/1/2018': 51.880000000000003},
    'after_strip_escalator_oil': 1.03,
    'price_oil_max': 65.0,
    'price_oil_flat': 47.0,
    'price_gas_strip': {'5/1/2019': 2.87, '5/1/2018': 2.84, '12/1/2028': 4.74, '5/1/2017': 2.85, '8/1/2028': 4.35, '8/1/2023': 3.51, '8/1/2022': 3.34, '8/1/2021': 3.18, '8/1/2020': 3.03, '8/1/2027': 4.19, '8/1/2026': 4.03, '8/1/2025': 3.86, '8/1/2024': 3.69, '11/1/2028': 4.54, '12/1/2021': 3.45, '12/1/2020': 3.3, '11/1/2020': 3.14, '11/1/2021': 3.3, '11/1/2022': 3.47, '11/1/2023': 3.64, '11/1/2024': 3.83, '11/1/2025': 4.01, '11/1/2026': 4.19, '11/1/2027': 4.37, '2/1/2028': 4.69, '3/1/2019': 3.17, '3/1/2018': 3.2, '2/1/2021': 3.41, '2/1/2020': 3.29, '2/1/2023': 3.73, '2/1/2022': 3.56, '3/1/2017': 3.08, '2/1/2024': 3.91, '2/1/2027': 4.49, '2/1/2026': 4.29, '10/1/2027': 4.26, '12/1/2027': 4.56, '10/1/2026': 4.1, '12/1/2026': 4.36, '10/1/2025': 3.93, '10/1/2024': 3.75, '8/1/2018': 2.92, '8/1/2019': 2.96, '8/1/2016': 2.45, '8/1/2017': 2.95, '7/1/2027': 4.15, '9/1/2019': 2.95, '9/1/2018': 2.91, '7/1/2024': 3.65, '7/1/2025': 3.82, '9/1/2017': 2.94, '9/1/2016': 2.5, '6/1/2025': 3.78, '6/1/2024': 3.61, '6/1/2027': 4.11, '6/1/2026': 3.94, '6/1/2021': 3.11, '6/1/2020': 2.97, '6/1/2023': 3.43, '6/1/2022': 3.27, '3/1/2026': 4.23, '3/1/2027': 4.42, '3/1/2024': 3.84, '3/1/2025': 4.03, '3/1/2022': 3.5, '3/1/2023': 3.66, '3/1/2020': 3.22, '3/1/2021': 3.34, '1/1/2022': 3.59, '1/1/2023': 3.76, '7/1/2026': 3.99, '2/1/2025': 4.1, '4/1/2028': 4.25, '4/1/2027': 4.09, '4/1/2026': 3.92, '4/1/2025': 3.76, '4/1/2024': 3.58, '4/1/2023': 3.41, '4/1/2022': 3.24, '4/1/2021': 3.08, '4/1/2020': 2.94, '7/1/2017': 2.93, '7/1/2016': 2.38, '11/1/2017': 3.04, '11/1/2016': 2.75, '11/1/2019': 3.05, '11/1/2018': 3.0, '12/1/2023': 3.79, '12/1/2022': 3.62, '12/1/2025': 4.17, '12/1/2024': 3.98, '7/1/2019': 2.94, '7/1/2018': 2.91, '1/1/2028': 4.71, '4/1/2017': 2.87, '1/1/2020': 3.32, '1/1/2021': 3.43, '4/1/2018': 2.87, '4/1/2019': 2.88, '1/1/2024': 3.93, '1/1/2025': 4.12, '1/1/2026': 4.32, '1/1/2027': 4.51, '3/1/2028': 4.62, '9/1/2020': 3.03, '9/1/2021': 3.18, '9/1/2022': 3.35, '9/1/2023': 3.52, '9/1/2024': 3.7, '9/1/2025': 3.87, '9/1/2026': 4.04, '9/1/2027': 4.21, '9/1/2028': 4.37, '6/1/2028': 4.27, '5/1/2024': 3.57, '5/1/2025': 3.75, '5/1/2026': 3.91, '5/1/2027': 4.07, '5/1/2020': 2.94, '5/1/2021': 3.08, '5/1/2022': 3.24, '5/1/2023': 3.4, '5/1/2028': 4.23, '10/1/2018': 2.93, '10/1/2019': 2.97, '10/1/2016': 2.57, '10/1/2017': 2.96, '2/1/2017': 3.13, '2/1/2018': 3.27, '2/1/2019': 3.23, '7/1/2028': 4.31, '10/1/2028': 4.42, '7/1/2022': 3.31, '7/1/2023': 3.47, '7/1/2020': 3.01, '7/1/2021': 3.15, '10/1/2023': 3.56, '10/1/2022': 3.38, '10/1/2021': 3.22, '10/1/2020': 3.07, '6/1/2018': 2.88, '6/1/2019': 2.91, '12/1/2016': 3.01, '12/1/2017': 3.19, '12/1/2018': 3.15, '12/1/2019': 3.2, '6/1/2017': 2.89, '1/1/2017': 3.13, '1/1/2019': 3.27, '1/1/2018': 3.3},
    'after_strip_escalator_gas': 1.03,
    'price_gas_max': 4.0,
    'price_gas_flat': 3.0,
    'price_ngl_strip': {},
    'price_ngl_flat': 0.0,
    'after_strip_escalator_ngl': 1.03,
    'price_ngl_max': 0.0,
    'working_interest': 1.0,
    'net_revenue_interest': .75,
    'discount_rate_annual': .10,
}

config=copy.copy(inputs)

for product, record in inputs['curves'].iteritems():
    if record !={}:
        if float(record['b_factor'])==1.0:
            config['curves'][product]['b_factor_adj']=1.001
        elif float(record['b_factor'])==0.0:
            config['curves'][product]['b_factor_adj']=0.001
        else:
            config['curves'][product]['b_factor_adj']=record['b_factor']

        config['curves'][product]['nominal_decline_monthly']=record['nominal_decline_annual']/12.0
        config['curves'][product]['Dmin_monthly']=record['Dmin_annual']/12.0

config['max_life_months']=inputs['max_life_years']*12
config['max_life_days']=inputs['max_life_years']*inputs['standard_days_in_year']