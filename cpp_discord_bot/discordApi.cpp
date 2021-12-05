#include <cstdlib>
#include <iostream>

int main() {
	//MyClientClass client("", SleepyDiscord::USER_CONTROLED_THREADS);
	//client.run();
    if(const char* env_p = std::getenv("HUNCHO_TOKEN"))
        std::cout << "HUNCHO_TOKEN: " << env_p << '\n';
    std::cout << "Fuck Justin\n";
}