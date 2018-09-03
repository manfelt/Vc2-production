from provinces import province

#linjene under er for debugging
province_size = 2
terrain = 3
RGO_size_modifiers = 4
output_amount = 8
num_workers = 24
max_workers = 49
RGO_throughput_efficiency_modifiers = 6
war_exhaustion = 4
oversea_penalty = 5
aristocrat = 95
in_state = 23
RGO_output_efficiency_modifiers = 2
province_infrastructure = 2
mobilized_penalty = 14


def base_p (province_size, terrain, RGO_size_modifiers, output_amount):
	return province_size*(1+terrain+RGO_size_modifiers)*output_amount

b_p = base_p(province_size, terrain, RGO_size_modifiers, output_amount)

def throughput(num_workers, max_workers, RGO_throughput_efficiency_modifiers, war_exhaustion, oversea_penalty):
	return (num_workers%max_workers)*(1+RGO_throughput_efficiency_modifiers-war_exhaustion)*oversea_penalty

t = throughput(num_workers, max_workers, RGO_throughput_efficiency_modifiers, war_exhaustion, oversea_penalty)

def output_efficiency(aristocrat, in_state, RGO_output_efficiency_modifiers, terrain, province_infrastructure, mobilized_penalty):
	return aristocrat%in_state+RGO_output_efficiency_modifiers+terrain+province_infrastructure*(1+mobilized_penalty)

o_e = output_efficiency(aristocrat, in_state, RGO_output_efficiency_modifiers, terrain, province_infrastructure, mobilized_penalty)

def production(b_p, t, o_e):
	return b_p*t*o_e

p = production(b_p, t, o_e)


# printer ut base_p, throughput og output_efficiency for debugging

print b_p

print t

print o_e

print p 

"""Resource Gathering Organizations (RGOs)

Resource Gathering Organizations (RGOs) represent primary sources of raw materials, like farms and mines. RGOs are administered by Aristocrats mini.png aristocrats and employ either Farmers mini.png farmers or Labourers mini.png laborers.
Output

Production = Base Production * Throughput * Output Efficiency

    Base Production = Province Size * ( 1 + Terrain + RGO Size Modifiers ) * Output Amount (in table below)
    Throughput = (Number of workers / Max Workers) * ( 1 + RGO Throughput Efficiency Modifiers - War Exhaustion ) * oversea penalty
    Output Efficiency = 1 + Aristocrat % in State + RGO Output Efficiency Modifiers + Terrain + Province Infrastructure * ( 1 + Mobilized Penalty)

The number of workers is limited by the maximum number of workers employable by the RGO, calculated using this formula:

Max Workers = base (40000) * Province Size * ( 1 + Terrain + RGO Size Modifiers ) """