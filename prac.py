def convert_duration(Duration):
        if len(Duration.split()) == 2:
            hours = int(Duration.split()[0][: -1])
            minutes = int(Duration.split()[1][: -1])
            return hours * 60 + minutes
        else:
            return int(Duration[: -1]) * 60
        
Duration = "9h 30m"
x = convert_duration(Duration)
print(x)
