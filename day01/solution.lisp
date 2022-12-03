(defvar total 0)

(defun sumlines () (write (loop (let ((input ""))
    (setq input (read))
    (when (not(> input -1)) (return total))
    (setq total (+ total input))))))

(sumlines)