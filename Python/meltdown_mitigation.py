def is_criticality_balanced(temperature, neutrons_emitted):
    product = temperature * neutrons_emitted
    if temperature < 800 and neutrons_emitted > 500 and product < 500000:
        return True
    return False
    
def reactor_efficiency(voltage, current, theoretical_max_power):
    power = voltage * current
    percentage = (power / theoretical_max_power) * 100
    if percentage >= 80:
        return "green"
    elif percentage < 80 and percentage >= 60:
        return "orange"
    elif percentage < 60 and percentage >= 30:
        return "red"
    else: return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    result = float(temperature) * float(neutrons_produced_per_second)
    percentage = (result * 100) / float(threshold)
    if percentage < 90.0:
        return "LOW"
    elif percentage >= 90.0 and percentage <= 110.0:
        return "NORMAL"
    else: return "DANGER"

fail_safe(10, 399, 10000)