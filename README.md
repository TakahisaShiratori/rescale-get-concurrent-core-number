# rescale-get-concurrent-core-number
User script to get the number of concurrent core for specific software on Rescale

## Usage

### Built Docker image locally

Clone this repository, and build the image
```bash
$ git clone git@github.com:TakahisaShiratori/rescale-get-concurrent-core-number.git
$ cd rescale-get-concurrent-core-number/
$ docker build -t rescale-get-concurrent-core-number .
```

Run the built image

RESCALE_API_KEY is required environmental variable.
```bash
$ docker run \
  -e RESCALE_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \
  rescale-get-concurrent-core-number
```

Use RESCALE_PLATFORM and TARGET_SOFTWARE to specify platform and software, respectively.
For example,
```bash
$ docker run \
  -e RESCALE_PLATFORM=platform.rescale.jp \
  -e RESCALE_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \
  -e TARGET_SOFTWARE=LS-DYNA \
  rescale-get-concurrent-core-number
```
