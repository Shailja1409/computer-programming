'''You are planning a trip and want to create an itinerary. You have a list of destinations, but they are all jumbled up. You want to print the destinations in alphabetical order so you can plan your trip better.

Problem: Write a Python program that takes a list of destinations and prints them in alphabetical order.

Example:

Input:
Paris Tokyo London NewYork

Output:
London NewYork Paris Tokyo  '''

def sort_destinations(destinations):
    destination_list = destinations.split()
    
    sorted_destinations = sorted(destination_list)
    
    print(" ".join(sorted_destinations))
    
input_destinations = "Paris Tokyo London NewYork"
sort_destinations(input_destinations)
