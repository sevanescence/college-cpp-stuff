# constants
CXX = clang++
CXXFLAGS = -Wall

SRC_DIR = examples
BUILD_DIR = debug

.SILENT: # disable echo-ing the commands

# rules
%.cpp: $(BUILD_DIR)/%.exe
	$^

$(BUILD_DIR)/%.exe: $(SRC_DIR)/%.cpp
	mkdir -p $(BUILD_DIR)
	
	$(CXX) $(CXXFLAGS) -o $@ $^

# targets
all: $(wildcard $(SRC_DIR)/*.cpp)
	$(MAKE) $(notdir $^)

clean:
	rm -rf $(BUILD_DIR)