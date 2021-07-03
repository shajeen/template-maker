<!-- ![spread](https://user-images.githubusercontent.com/2623563/124358707-2105a300-dc3f-11eb-9173-f7132130ed02.png) -->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/shajeen/template-maker/blob/package/README.md">
    <img src="https://user-images.githubusercontent.com/2623563/124358707-2105a300-dc3f-11eb-9173-f7132130ed02.png" alt="Logo" width="640" height="320">
  </a>

  <h3 align="center">template-maker</h3>

  <p align="center">
    An awesome tool to help in your projects!
    <br />
    <a href="https://github.com/shajeen/template-maker/wiki"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/shajeen/template-maker/issues/new?assignees=shajeen&labels=bug&template=bug_report.md&title=">Report Bug</a>
    ·
    <a href="https://github.com/shajeen/template-maker/issues/new?assignees=shajeen&labels=enhancement&template=feature_request.md&title=">Request Feature</a>
  </p>
</p>


## About The Project
![Screenshot from 2021-07-03 20-49-54](https://user-images.githubusercontent.com/2623563/124358944-4515b400-dc40-11eb-8d08-6b792cd2a000.png)

There are many great tools available on GitHub, however, I didn't find one that really suit my needs so I created this enhanced one. I want to create a tool which make me better.

## Getting Started

Follow the instructions to setting up project locally.
To get a local copy up and running follow these steps.

### Installation

 Install from the git repo
   ```sh
   pip install https://github.com/shajeen/template-maker.git
   ```
 
 Install from pypi 
   ```sh
   pip install template-maker
   ```
   more information at https://pypi.org/project/template-maker/
  
### How it works

There are two argument required, --name and --ptype. 

 - **--name** - Your project name
 - **--ptype** - Type of your project, application or library.

| ptype | value |
| :--:  | :--:  |
| App   |   0   |
| Lib   |   1   |

### **Application mode with CMake conan support**
```sh
template-maker --name="sample_application" --ptype=0
```
***working example***

![Screenshot from 2021-07-03 21-01-06](https://user-images.githubusercontent.com/2623563/124359267-d3d70080-dc41-11eb-89d3-172573c40dbb.png)

***Generated output***

![Screenshot from 2021-07-03 20-57-44](https://user-images.githubusercontent.com/2623563/124359157-62974d80-dc41-11eb-882f-0f203fc3c62b.png)

### **Library mode with CMake conan support**
```sh
template-maker --name="sample_library" --ptype=1
```
***working example***

![Screenshot from 2021-07-03 21-02-54](https://user-images.githubusercontent.com/2623563/124359332-1dbfe680-dc42-11eb-94ab-b41ce0ce7eec.png)

***Generated output***

![Screenshot from 2021-07-03 21-03-10](https://user-images.githubusercontent.com/2623563/124359344-2adcd580-dc42-11eb-919b-a92b1a1d8d27.png)

## Roadmap

See the [open issues](https://github.com/shajeen/spreadsheet-to-cpplib/issues) for a list of proposed features (and known issues).

### Contributing

Any contributions you make are **greatly appreciated**.

1. Create an issue describing your changes.
2. Fork the repo, make the changes and please dont forget to test.
3. Create the pull request. 

Please read the [CONTRIBUTING](https://github.com/shajeen/template-maker/blob/main/CONTRIBUTING.md) before raising the PR.

## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

## Contact

 - Shajeen Ahamed - [@shajeenahamed](https://twitter.com/shajeenahamed) - shajeenahmed@gmail.com
 - Project Link: [https://github.com/shajeen/template-maker](https://github.com/shajeen/template-maker)

