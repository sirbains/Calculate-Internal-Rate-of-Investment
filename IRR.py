def calc_irr(cash_flows, initial_investment=0):
  """
  Calculates the internal rate of return (IRR) of an investment.
  
  Parameters:
  cash_flows (list of floats): the cash flows of the investment, with the initial investment as the first element and the subsequent cash flows as the following elements
  initial_investment (float, optional): the initial investment in the project (default is 0)
  
  Returns:
  float: the internal rate of return of the investment
  """
  def npv(rate, cash_flows, initial_investment):
    """
    Calculates the net present value (NPV) of an investment.
    
    Parameters:
    rate (float): the discount rate
    cash_flows (list of floats): the cash flows of the investment, with the initial investment as the first element and the subsequent cash flows as the following elements
    initial_investment (float): the initial investment in the project
    
    Returns:
    float: the net present value of the investment
    """
    npv = initial_investment
    for i, cash_flow in enumerate(cash_flows):
      npv += cash_flow / (1 + rate) ** (i + 1)
    return npv
  
  # Set the initial bounds for the IRR
  lower_bound = -1.0
  upper_bound = 1.0
  
  # Iteratively narrow down the bounds until the IRR is found
  while upper_bound - lower_bound > 1e-10:
    rate = (lower_bound + upper_bound) / 2
    npv_value = npv(rate, cash_flows, initial_investment)
    if npv_value > 0:
      lower_bound = rate
    else:
      upper_bound = rate
  
  # Return the IRR
  return rate

# Example usage
cash_flows = [-100, 50, 60, 70]
irr = calc_irr(cash_flows)
print(f"The IRR of the investment is {irr:.2f}")
