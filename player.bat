@echo off 
    cd musics
    for /R %%x in (*) do ( 
        call "%%x"
        pause
        )
pause