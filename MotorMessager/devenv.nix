{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/packages/
  packages = with pkgs; [
    git
    (python312.withPackages (ps: with ps; [ pyserial ]))
  ];

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    version = "3.12";
    venv = {
      enable = true;
      requirements = ''
        pyserial
      '';
    };
  };
}
