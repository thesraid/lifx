#!/usr/bin/env python

import argparse
import requests

#########################################################################################################

def get_args():
    """Get command line args from the user.
    """
    parser = argparse.ArgumentParser(
        description='Turn lights on and off')

    parser.add_argument('-l', '--light',
                        required=False,
                        default='all',
                        action='store',
                        help='Lights up|down')

    parser.add_argument('-p', '--power',
                        required=False,
                        default='off',
                        action='store',
                        help='Power on|off')

    args = parser.parse_args()

    return args

#########################################################################################################

def main():

   headers = {
       "Authorization": "Bearer cf04eb27b53d785ce523aecebc32b0d2e3cd454307939022ddaa849f3c9f3b3c",
   }

   # Get the command line argumants and store them in the args variable
   args = get_args()

   # Assign each argument to a variable
   light=args.light
   power=args.power

   if light == "up":
      light = "d073d50145fa"
   elif light == "down":
      light = "d073d5014340"

   if power == "on":
      payload = {
          "power": "on",
      }
   elif power == "off":
      payload = {
          "power": "off",
      }          

   response = requests.put('https://api.lifx.com/v1/lights/' + light + '/state', headers=headers, data=payload)
   print response.text
#########################################################################################################

# Start program
if __name__ == "__main__":
    main()

#########################################################################################################
