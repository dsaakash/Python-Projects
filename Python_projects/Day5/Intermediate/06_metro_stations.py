"""
Intermediate Project 6: Metro Stations
Concepts: Finding index distances, slicing routes.
"""

def display_route(route):
    print(" -> ".join(route))

def run_metro_app():
    # Linear metro line
    stations = ["Station A", "Station B", "Station C", "Station D", "Station E", "Station F"]
    
    print("--- Metro Route Planner ---")
    print("Line 1 Stations:")
    display_route(stations)
    
    start_station = input("\\nEnter starting station (e.g. Station B): ").strip()
    end_station = input("Enter destination station (e.g. Station E): ").strip()
    
    if start_station in stations and end_station in stations:
        start_idx = stations.index(start_station)
        end_idx = stations.index(end_station)
        
        # Calculate number of stops
        stops = abs(end_idx - start_idx)
        print(f"\\nNumber of stops: {stops}")
        
        print("Your Route:")
        if start_idx < end_idx:
            # Traveling forward: Slicing from start to end
            route = stations[start_idx:end_idx + 1]
            display_route(route)
        elif start_idx > end_idx:
            # Traveling backward: Slicing and reversing
            # Slice from end to start, then reverse it
            route = stations[end_idx:start_idx + 1]
            route.reverse()
            display_route(route)
        else:
            print("You are already at your destination!")
            
    else:
        print("Invalid station(s) entered.")

if __name__ == "__main__":
    run_metro_app()
