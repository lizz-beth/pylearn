from weather import weather_data
from timed import write_and_sleep
from date import current_time_formatted
import coords
import formatting
import weather_queries

dir = "files/weather.txt"

while True:
    formatted_time = current_time_formatted()
    write_and_sleep(
        dir,
        "{}\n{}\n\n{}".format(
            formatted_time,
            "_" * len(str(formatted_time)),
            formatting.prettier(
                weather_data(
                    weather_queries.coord_query(
                        *coords.current()
                    )
                )
            )
        ),
        300
    )
