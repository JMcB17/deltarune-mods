import shutil
from pathlib import Path


REPACK_DIR_NAME = '_repack'
IMAGE_FORMAT = '.png'


def process_sprite(sprite: Path, repack_dir: Path, multi: bool = False):
    if multi:
        dir_name = sprite.parent.stem
        new_sprite_name = dir_name + '_' + sprite.stem
    else:
        new_sprite_name = sprite.stem + '_0'

    print(new_sprite_name)
    new_sprite_path = repack_dir.joinpath(new_sprite_name).with_suffix(IMAGE_FORMAT)

    shutil.copy(sprite, new_sprite_path)


def process_dir(directory: Path, repack_dir: Path, level: int = 0):
    dir_name = directory.stem

    for sprite in directory.iterdir():
        if sprite.is_dir():
            if not sprite.name == REPACK_DIR_NAME:
                process_dir(sprite, repack_dir, level=level + 1)
        
        if sprite.suffix == IMAGE_FORMAT:
            process_sprite(sprite, repack_dir, multi=(level != 0))


def main():
    pwd = Path().resolve()
    repack_dir_path = pwd / REPACK_DIR_NAME

    process_dir(pwd, repack_dir_path)


if __name__ == '__main__':
    main()
