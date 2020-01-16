#!/bin/bash

for string in "hi" "HELLO" "WORLD" "hello" "world" "wow" "awesome" "start" "end" "etc"; do
    case ${string} in
        hello|HELLO)
            echo "hello or HELLO : ${string}"
            ;;
        wo*)
            echo "wo로 시작하는 단어 : ${string}"
            ;;
        a*|end)
            echo "a로 시작하는 단어 or end일 때 : ${string}"
            ;;
        *)
            echo "기타 : ${string}"
            ;;
    esac
done
