# put-programs-here/FIRESTARTER

## Building from source

```bash
# install prerequisites
sudo apt update
sudo apt install build-essential cmake git pkg-config
mkdir build-firestarter
pushd build-firestarter
git clone https://github.com/tud-zih-energy/FIRESTARTER.git
cd FIRESTARTER
mkdir build
cd build
# NOTE: don't bother with build tests or fetching GoogleTest, not necessary for building.
cmake -DFIRESTARTER_BUILD_TESTS=OFF -DFIRESTARTER_FETCH_GOOGLETEST=OFF ..
make -j$(nproc) # use all CPU cores to speed up compilation
./src/FIRESTARTER -t 1 # quickly run a 1 second stress-test to test the binary
popd
install -m 755 ./build-firestarter/FIRESTARTER/build/src/FIRESTARTER ./put-programs-here/FIRESTARTER/FIRESTARTER
```
