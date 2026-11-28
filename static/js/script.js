const archivo = document.getElementById("foto_archivo");

if (archivo) {
    const oculto = document.getElementById("foto");
    const vista = document.getElementById("vista_previa");

    archivo.addEventListener("change", function () {
        const file = archivo.files[0];

        if (!file) {
            oculto.value = "";
            vista.src = vista.dataset.original;
            return;
        }

        const lector = new FileReader();

        lector.onload = function () {
            const img = new Image();

            img.onload = function () {
                const maximo = 200;
                const escala = Math.min(1, maximo / Math.max(img.width, img.height));

                const canvas = document.createElement("canvas");
                canvas.width = img.width * escala;
                canvas.height = img.height * escala;

                const ctx = canvas.getContext("2d");
                ctx.fillStyle = "#ffffff";
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

                const foto = canvas.toDataURL("image/jpeg", 0.8);
                oculto.value = foto;
                vista.src = foto;
            };

            img.src = lector.result;
        };

        lector.readAsDataURL(file);
    });

    archivo.form.addEventListener("reset", function () {
        oculto.value = "";
        vista.src = vista.dataset.original;
    });
}
