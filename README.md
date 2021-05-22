
  
## Utilities to make your work easy    
 ### Setup
 - Clone this repo    
 - Have Python installed
     
### Installation 
```python 
pip install requests
pip install kafka-python
```    

`Note: use pip3 if you have python3 installed`    
 
### VPNs  
  
Make sure you are connected to 

 1. GOJEK Integration
 2. GOPAY staging 
  
### Usage    
 - To create a new user    
   ```python    
   python3 GenerateUser.py | python3 -m json.tool    
   ```    
 - To set GoPay pin    
   ```python    
   python3 SetGoPayPin.py <email> <OTP you want to set>    
   ```    
       
 Example:     
 ```  
 python3 SetGoPayPin.py somemail@id.com 123456
 ```  
  and wait for the a success output, if success is false try setting up the pin again    
       
  you should see something like    
  ```
  {'success': True, 'errors': None}
```