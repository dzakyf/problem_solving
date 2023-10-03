const denominator = {
  "ONE HUNDRED": 100,
  "TWENTY": 20,
  "TEN" : 10,
  "FIVE" : 5,
  "ONE" : 1,
  "QUARTER": 0.25,
  "DIME" : 0.1,
  "NICKEL": 0.05,
  "PENNY" : 0.01,
}

const INSUFFICIENT = "INSUFFICIENT_FUNDS"
const OPEN = "OPEN"
const CLOSED = "CLOSED"

function checkBalanceRegister(cid){
  let balance = {
    total : 0,
  }

  for(let i = 0; i < cid.length; ++i){
    balance.total += cid[i][1]
    balance[cid[i][0]] = cid[i][1]
  }

  return balance
}



function checkCashRegister(price, cash, cid) {
  let remainder = cash - price
  let res = {
    status : "",
    change: [],
  }

  //Check total balance on register
  let totalRegisterBalance = checkBalanceRegister(cid)
//   console.log(totalRegisterBalance)
  if(totalRegisterBalance.total < remainder){
    res.status = INSUFFICIENT
    // console.log(res)
    return res
  }

  if(totalRegisterBalance.total === remainder){ 
    res.status = CLOSED
    res.change = cid
    // console.log(res)
    return res
  }

  //calculate change 
  let changes = []

  for(let key in denominator){
    let value = 0 
    // console.log(key, denominator[key])
    while(totalRegisterBalance[key] > 0 && remainder >= denominator[key]){
        // console.log(totalRegisterBalance, remainder, denominator)
        remainder -= denominator[key]
        totalRegisterBalance[key] -= denominator[key]
        value += denominator[key] 
        remainder = Math.round(remainder*100) / 100
    }
    if(value > 0){ 
        // console.log(value)
        changes.push([key, value])
    }
    // console.log(changes)
    // changes.push(key, denominator[key])
  }

  if(changes.length < 1 || remainder > 0) {
    res.status = INSUFFICIENT
    console.log(res)
    return res
  }
 

  res.status = OPEN
  res.change = changes

//   console.log(changes)
  return res;
}

// checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
// checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]) 
// checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]])
// checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]) 
checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]])
