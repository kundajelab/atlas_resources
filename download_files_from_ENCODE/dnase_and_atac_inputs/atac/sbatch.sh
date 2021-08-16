for i in `seq 0 733` 
do 
sbatch -p akundaje,owners,normal -o logs/$i.o -e logs/$i.e -J $i --time=240 ./x$i
done

