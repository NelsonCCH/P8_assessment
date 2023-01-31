import React, { useState, Fragment } from 'react';
import 'semantic-ui-css/semantic.min.css';
import { Dropdown } from 'semantic-ui-react'

function App() {

    const [payment, setPayment] = useState(0);
    const [inputs, setInputs] = useState({});

    // submit get request to backend endpoint, give alert and error hints for invalid inputs
    const handleSubmit = async (event) => {
      event.preventDefault();
      let response = await fetch('/calculate_mortgage_payment?', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(inputs)
      })

      let result = await response.json()
      if (response.ok) {
        setPayment(result)
      } else {
        alert(`Response not 200, please try again. \nError: ${result}`)
      }
    }

    // convert inputs into float if they are numbers
    const handleInputChange = (e) => {
      setInputs({...inputs, [e.target.name]: e.target.type === 'number' ? parseFloat(e.target.value) : e.target.value});
    };
  
    // for dropdown menu's options
    const payment_options = [
      {
        key: 'monthly',
        text: 'monthly',
        value: 'monthly'
      },
      {
        key: 'bi-weekly',
        text: 'bi-weekly',
        value: 'bi_weekly'
      },
      {
        key: 'accelerated bi-weekly',
        text: 'accelerated bi-weekly',
        value: 'accelerated_bi_weekly'
      }
    ]

    return (
      <div>
        <form onSubmit={handleSubmit}>

          <label> Property Price: </label>
          <input required type="number" name="price" min="0" onChange={handleInputChange}/><br></br>

          <label> Down payment: </label>
          <input required type="number" name="down_payment" min="0" max={inputs.price} onChange={handleInputChange}/><br></br>

          <label> Interest Rate: </label>
          <input required type="number" name="rate" min="0" max="100" step="0.01" onChange={handleInputChange}/><br></br>
          
          <label> Amortization Period: </label>
          <input required type="number" name="amortization" min="5" max="25" step="5"onChange={handleInputChange}/><br></br>
          
          <label>Payment_schedule: </label>
          <Dropdown
            required
            name="payment_schedule"
            placeholder='Select Payment Schedule'
            selection
            options={payment_options}
            onChange={(e,data) => {setInputs({...inputs, [data.name]: data.value})}}
          />
          <br></br>
          <button type="submit"> Submit </button>
        </form>
        <p>Your payment per payment schedule is {payment}</p>
      </div>
    );
}

export default App;
